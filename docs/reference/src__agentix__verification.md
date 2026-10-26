# Reference for src/agentix/verification.py

Per-runtime, content-bound observations; model output never creates evidence.

Provisional unittest reports alone never authorize execution. Additional host
acceptance records bind a human-reviewed contract, covered functions and evaluator
version to exact artifact bytes. Successful calls establish bounded session grants
and, when configured, Windows-protected durable approvals. Result receipts remain query-bound. Finite cases do not prove
all-input correctness.

Source fingerprint: 15a9fc0f6ce1d46cae80b8edc16b1a2d92a4a60d3270bdc44b56068869b9eb0a

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### VerificationLedger

Own query receipts, bounded session grants and injected durable approval storage.

Kind: class. Declared return: Not declared / class. Source line: 25.

### VerificationLedger.__init__

Bind evidence to one approval owner and its current operation.

Kind: callable. Declared return: None. Source line: 28.

### VerificationLedger.snapshot

Read only the two explicitly validated runtime artifacts, never import.

Kind: callable. Declared return: tuple[bytes, bytes]. Source line: 42.

### VerificationLedger._identity

Separate owner/run identity from an unambiguous length-framed digest.

Kind: callable. Declared return: tuple[str, str, bytes]. Source line: 58.

### VerificationLedger.invalidate

Revoke previous evidence before any new pipeline or test attempt.

Kind: callable. Declared return: None. Source line: 63.

### VerificationLedger.record

Accept only nonempty, unskipped successful observations of current bytes.

Kind: callable. Declared return: bool. Source line: 74.

### VerificationLedger.is_provisional

Check current unittest observations; these never authorize execution.

Kind: callable. Declared return: bool. Source line: 119.

### VerificationLedger.authorize

Publish host acceptance after human review; never call from child reports.

This is an internal trusted service boundary, not a model-facing tool.
Its caller must compare every approved case in the host evaluator first.

Kind: callable. Declared return: bool. Source line: 140.

### VerificationLedger._revoke_stored

Best-effort disk revocation; never expose native/filesystem exception bodies.

Kind: callable. Declared return: None. Source line: 176.

### VerificationLedger.revoke_acceptance

Revoke human acceptance while retaining a current provisional observation.

Kind: callable. Declared return: None. Source line: 186.

### VerificationLedger.acceptance_context

Return defensive reviewed data and AST signatures for the final manager.

Only currently accepted bytes are parsed; no generated module is imported.
The evaluator owns contract validation and host comparison before publication.

Kind: callable. Declared return: dict[str, Any] | None. Source line: 195.

### VerificationLedger.begin_execution

Clear earlier results even when a new call fails input validation.

Kind: callable. Declared return: None. Source line: 222.

### VerificationLedger.has_execution_activity

Identify current-operation tool workflows without parsing model prose.

Kind: callable. Declared return: bool. Source line: 228.

### VerificationLedger.record_execution

Record an isolated call observation after dispatch, never model prose.

The trusted executor must validate process success first. Recheck exact
source/acceptance after the child returns; revoke on edits during execution.
Retain one bounded child result and a defensive copy of JSON arguments.

Kind: callable. Declared return: bool. Source line: 236.

### VerificationLedger.prepare_reuse

Rebind a successful reviewed tool to this query without running tests.

Grants come from successful host-accepted calls in this session or the
injected protected store. Cross-session reuse never transfers a result
receipt. Exact bytes, policy and covered functions are checked; observed
drift or explicit revocation removes trust. Closing one session does not
revoke a durable approval owned by the Windows user.

Kind: callable. Declared return: bool. Source line: 297.

### VerificationLedger.execution_result

Return a current host-observed call or nothing; stale evidence is revoked.

Kind: callable. Declared return: dict[str, Any] | None. Source line: 352.

### VerificationLedger.is_verified

Require host acceptance for the current bytes, owner, run and function.

Kind: callable. Declared return: bool. Source line: 369.

### VerificationLedger.matches

Check the exact snapshot about to execute, avoiding a path-based race.

Kind: callable. Declared return: bool. Source line: 381.

### VerificationLedger.matches_authorized

Atomically recheck both acceptance and the exact snapshot before dispatch.

Kind: callable. Declared return: bool. Source line: 386.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ast | Imported dependency for ast in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | copy | Imported dependency for copy in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | ApprovalStore | Imported dependency for ApprovalStore in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | SecurityBoundary | Imported dependency for SecurityBoundary in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 22 |
| VerificationLedger.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 28 |
| VerificationLedger.__init__ | security | Owner-scoped approval and path boundary injected into this service. | SecurityBoundary | Enclosing invocation or class/instance lifetime | 28 |
| VerificationLedger.__init__ | store | Parameter for store in VerificationLedger.__init__; use the enclosing contract and type below. | ApprovalStore &#124; None | Enclosing invocation or class/instance lifetime | 28 |
| VerificationLedger.__init__ | self.security | Owner-scoped approval and path boundary injected into this service. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 30 |
| VerificationLedger.__init__ | self.store | Attribute for store in VerificationLedger.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 31 |
| VerificationLedger.__init__ | self._owner | Attribute for owner in VerificationLedger.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 32 |
| VerificationLedger.__init__ | self._lock | Attribute for lock in VerificationLedger.__init__; use the enclosing contract and type below. | Return type of RLock; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| VerificationLedger.__init__ | self._records | Attribute for records in VerificationLedger.__init__; use the enclosing contract and type below. | dict[str, tuple[str, str, bytes]] | Enclosing invocation or class/instance lifetime | 34 |
| VerificationLedger.__init__ | self._acceptance | Attribute for acceptance in VerificationLedger.__init__; use the enclosing contract and type below. | dict[str, tuple[tuple[str, str, bytes], str, frozenset[str], str]] | Enclosing invocation or class/instance lifetime | 35 |
| VerificationLedger.__init__ | self._contracts | Attribute for contracts in VerificationLedger.__init__; use the enclosing contract and type below. | dict[str, dict[str, Any]] | Enclosing invocation or class/instance lifetime | 36 |
| VerificationLedger.__init__ | self._execution | Attribute for execution in VerificationLedger.__init__; use the enclosing contract and type below. | tuple[tuple[str, str, bytes], str, dict[str, Any]] &#124; None | Enclosing invocation or class/instance lifetime | 37 |
| VerificationLedger.__init__ | self._attempt | Attribute for attempt in VerificationLedger.__init__; use the enclosing contract and type below. | tuple[str, str] &#124; None | Enclosing invocation or class/instance lifetime | 38 |
| VerificationLedger.__init__ | self._reuse | Attribute for reuse in VerificationLedger.__init__; use the enclosing contract and type below. | dict[str, tuple[str, bytes, bytes, str, frozenset[str], dict[str, Any]]] | Enclosing invocation or class/instance lifetime | 40 |
| VerificationLedger.snapshot | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| VerificationLedger.snapshot | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 42 |
| VerificationLedger.snapshot | paths | Local binding for paths in VerificationLedger.snapshot; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 44 |
| VerificationLedger.snapshot.comprehension_44 | part | Comprehension item for part in VerificationLedger.snapshot.comprehension_44; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 46 |
| VerificationLedger.snapshot | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | list | Enclosing invocation or class/instance lifetime | 49 |
| VerificationLedger.snapshot | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 50 |
| VerificationLedger.snapshot | stream | Managed resource for stream in VerificationLedger.snapshot; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 51 |
| VerificationLedger.snapshot | data | Local binding for data in VerificationLedger.snapshot; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
| VerificationLedger._identity | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 58 |
| VerificationLedger._identity | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 58 |
| VerificationLedger._identity | tests | Optional unittest source snapshot; child-authored success remains provisional. | bytes | Enclosing invocation or class/instance lifetime | 58 |
| VerificationLedger._identity | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of digest; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| VerificationLedger.invalidate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| VerificationLedger.invalidate | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 63 |
| VerificationLedger.invalidate | self._execution | Attribute for execution in VerificationLedger.invalidate; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 72 |
| VerificationLedger.record | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 75 |
| VerificationLedger.record | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 76 |
| VerificationLedger.record | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 77 |
| VerificationLedger.record | tests | Optional unittest source snapshot; child-authored success remains provisional. | bytes | Enclosing invocation or class/instance lifetime | 78 |
| VerificationLedger.record | report | Parameter for report in VerificationLedger.record; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 79 |
| VerificationLedger.record | isolated | Parameter for isolated in VerificationLedger.record; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 81 |
| VerificationLedger.record | exit_code | Parameter for exit code in VerificationLedger.record; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 82 |
| VerificationLedger.record | counts | Local binding for counts in VerificationLedger.record; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 86 |
| VerificationLedger.record | valid | Local binding for valid in VerificationLedger.record; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 87 |
| VerificationLedger.record.comprehension_93 | key | Comprehension item for key in VerificationLedger.record.comprehension_93; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 93 |
| VerificationLedger.record.comprehension_96 | key | Comprehension item for key in VerificationLedger.record.comprehension_96; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 96 |
| VerificationLedger.record | current | Local binding for current in VerificationLedger.record; use the enclosing contract and type below. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 109 |
| VerificationLedger.is_provisional | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 119 |
| VerificationLedger.is_provisional | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 119 |
| VerificationLedger.is_provisional | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 123 |
| VerificationLedger.is_provisional | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 123 |
| VerificationLedger.is_provisional | grant | Local binding for grant in VerificationLedger.is_provisional; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
| VerificationLedger.authorize | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 141 |
| VerificationLedger.authorize | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 142 |
| VerificationLedger.authorize | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 143 |
| VerificationLedger.authorize | tests | Optional unittest source snapshot; child-authored success remains provisional. | bytes | Enclosing invocation or class/instance lifetime | 144 |
| VerificationLedger.authorize | contract_digest | Parameter for contract digest in VerificationLedger.authorize; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 145 |
| VerificationLedger.authorize | functions | Parameter for functions in VerificationLedger.authorize; use the enclosing contract and type below. | frozenset[str] | Enclosing invocation or class/instance lifetime | 146 |
| VerificationLedger.authorize | reviewed_contract | Parameter for reviewed contract in VerificationLedger.authorize; use the enclosing contract and type below. | dict[str, Any] &#124; None | Enclosing invocation or class/instance lifetime | 148 |
| VerificationLedger.authorize | self._execution | Attribute for execution in VerificationLedger.authorize; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 166 |
| VerificationLedger._revoke_stored | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 176 |
| VerificationLedger._revoke_stored | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 176 |
| VerificationLedger._revoke_stored | exc | Caught exception for exc in VerificationLedger._revoke_stored; use the enclosing contract and type below. | (OSError, ValueError) | Current exception handler; Python clears this binding afterward | 181 |
| VerificationLedger.revoke_acceptance | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 186 |
| VerificationLedger.revoke_acceptance | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 186 |
| VerificationLedger.revoke_acceptance | self._execution | Attribute for execution in VerificationLedger.revoke_acceptance; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 193 |
| VerificationLedger.acceptance_context | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 195 |
| VerificationLedger.acceptance_context | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 195 |
| VerificationLedger.acceptance_context | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 204 |
| VerificationLedger.acceptance_context | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 204 |
| VerificationLedger.acceptance_context | approved | Local binding for approved in VerificationLedger.acceptance_context; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 205 |
| VerificationLedger.acceptance_context | functions | Local binding for functions in VerificationLedger.acceptance_context; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 208 |
| VerificationLedger.acceptance_context | node | Loop item for node in VerificationLedger.acceptance_context; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 209 |
| VerificationLedger.acceptance_context | signature | Local binding for signature in VerificationLedger.acceptance_context; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 211, 213 |
| VerificationLedger.begin_execution | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 222 |
| VerificationLedger.begin_execution | self._execution | Attribute for execution in VerificationLedger.begin_execution; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 225 |
| VerificationLedger.begin_execution | self._attempt | Attribute for attempt in VerificationLedger.begin_execution; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 226 |
| VerificationLedger.has_execution_activity | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 228 |
| VerificationLedger.has_execution_activity | identity | Explicit owner identity used by a session factory or fixture. | tuple | Enclosing invocation or class/instance lifetime | 231 |
| VerificationLedger.has_execution_activity.comprehension_232 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 233 |
| VerificationLedger.record_execution | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 237 |
| VerificationLedger.record_execution | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 238 |
| VerificationLedger.record_execution | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 239 |
| VerificationLedger.record_execution | tests | Optional unittest source snapshot; child-authored success remains provisional. | bytes | Enclosing invocation or class/instance lifetime | 240 |
| VerificationLedger.record_execution | function_name | Public callable selected for the current operation; empty selects test mode. | str | Enclosing invocation or class/instance lifetime | 241 |
| VerificationLedger.record_execution | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | dict[str, Any] | Enclosing invocation or class/instance lifetime | 242 |
| VerificationLedger.record_execution | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | str | Enclosing invocation or class/instance lifetime | 243 |
| VerificationLedger.record_execution | self._execution | Attribute for execution in VerificationLedger.record_execution; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 257, 259 |
| VerificationLedger.record_execution | approved | Local binding for approved in VerificationLedger.record_execution; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 269 |
| VerificationLedger.record_execution | exc | Caught exception for exc in VerificationLedger.record_execution; use the enclosing contract and type below. | (OSError, ValueError, TypeError) | Current exception handler; Python clears this binding afterward | 289 |
| VerificationLedger.prepare_reuse | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 297 |
| VerificationLedger.prepare_reuse | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 297 |
| VerificationLedger.prepare_reuse | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 311 |
| VerificationLedger.prepare_reuse | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 311 |
| VerificationLedger.prepare_reuse | stored | Local binding for stored in VerificationLedger.prepare_reuse; use the enclosing contract and type below. | Return type of load; see its callable contract | Enclosing invocation or class/instance lifetime | 312 |
| VerificationLedger.prepare_reuse | exc | Caught exception for exc in VerificationLedger.prepare_reuse; use the enclosing contract and type below. | (OSError, ValueError) | Current exception handler; Python clears this binding afterward | 313 |
| VerificationLedger.prepare_reuse | grant | Local binding for grant in VerificationLedger.prepare_reuse; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 331 |
| VerificationLedger.prepare_reuse | current | Local binding for current in VerificationLedger.prepare_reuse; use the enclosing contract and type below. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 335 |
| VerificationLedger.prepare_reuse | identity | Explicit owner identity used by a session factory or fixture. | Return type of _identity; see its callable contract | Enclosing invocation or class/instance lifetime | 346 |
| VerificationLedger.execution_result | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 352 |
| VerificationLedger.execution_result | identity | Explicit owner identity used by a session factory or fixture. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 357 |
| VerificationLedger.execution_result | digest | Content fingerprint for change detection; not a substitute for human approval. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 357 |
| VerificationLedger.execution_result | observation | Local binding for observation in VerificationLedger.execution_result; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 357 |
| VerificationLedger.execution_result | name | Current identifier selected by parsing, lookup or dependency registration. | tuple | Enclosing invocation or class/instance lifetime | 358 |
| VerificationLedger.execution_result | function | Local binding for function in VerificationLedger.execution_result; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 358 |
| VerificationLedger.execution_result | self._execution | Attribute for execution in VerificationLedger.execution_result; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 365 |
| VerificationLedger.is_verified | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 369 |
| VerificationLedger.is_verified | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 369 |
| VerificationLedger.is_verified | function_name | Public callable selected for the current operation; empty selects test mode. | str &#124; None | Enclosing invocation or class/instance lifetime | 369 |
| VerificationLedger.is_verified | approved | Local binding for approved in VerificationLedger.is_verified; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 372 |
| VerificationLedger.matches | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 381 |
| VerificationLedger.matches | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 381 |
| VerificationLedger.matches | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 381 |
| VerificationLedger.matches | tests | Optional unittest source snapshot; child-authored success remains provisional. | bytes | Enclosing invocation or class/instance lifetime | 381 |
| VerificationLedger.matches_authorized | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 387 |
| VerificationLedger.matches_authorized | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 387 |
| VerificationLedger.matches_authorized | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 387 |
| VerificationLedger.matches_authorized | tests | Optional unittest source snapshot; child-authored success remains provisional. | bytes | Enclosing invocation or class/instance lifetime | 387 |
| VerificationLedger.matches_authorized | function_name | Public callable selected for the current operation; empty selects test mode. | str | Enclosing invocation or class/instance lifetime | 387 |
