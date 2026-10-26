# Reference for src/agentix/acceptance.py

Human-reviewed declarative cases and host-owned deterministic verdicts.

Generated unittest counts are only provisional. Only this maintained evaluator
compares approved expectations with isolated observations and requests execution
authorization. Expected values and the acceptance contract never enter a child.

Source fingerprint: 59deec6dba176b03632b547f1bfd559369d3d2e25da9259d038d7be64fcc8690

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _unique

Reject ambiguous duplicate JSON keys at every nesting level.

Kind: callable. Declared return: dict[str, Any]. Source line: 25.

### validate_json

Bound JSON nesting/values and reject nonfinite or non-data objects.

Kind: callable. Declared return: None. Source line: 35.

### parse_contract

Parse bounded version-1 data only; executable assertions are unsupported.

Kind: callable. Declared return: dict[str, Any]. Source line: 56.

### _same

Compare recursively without Python's boolean/numeric equality coercion.

Kind: callable. Declared return: bool. Source line: 123.

### matches_expectation

Compare data outside the child; a child success/count assertion is irrelevant.

Kind: callable. Declared return: bool. Source line: 136.

### AcceptanceEvaluator

Coordinate mandatory human review and compare fresh isolated observations.

Kind: class. Declared return: Not declared / class. Source line: 164.

### AcceptanceEvaluator.__init__

Bind one session's review, backend and authorization ledger.

Kind: callable. Declared return: None. Source line: 167.

### AcceptanceEvaluator.status

Return an independent display snapshot; never reveal a capability token.

Kind: callable. Declared return: dict[str, Any]. Source line: 177.

### AcceptanceEvaluator.note_provisional

Display automatic checks separately from human/final acceptance.

Kind: callable. Declared return: None. Source line: 185.

### AcceptanceEvaluator._set

Publish a coherent stage and log only the fixed stage event.

Kind: callable. Declared return: None. Source line: 198.

### AcceptanceEvaluator.submit

Review generated cases and authorize only host-compared human-approved data.

Kind: callable. Declared return: str. Source line: 204.

### AcceptanceEvaluator._submit

Keep expected values exclusively in the trusted parent process.

Kind: callable. Declared return: str. Source line: 221.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | math | Imported dependency for math in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | deepcopy | Imported dependency for deepcopy in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | ExecutionBackend | Imported dependency for ExecutionBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | SecurityBoundary | Imported dependency for SecurityBoundary in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | VerificationLedger | Imported dependency for VerificationLedger in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 21 |
| module | _NAME | Module binding for NAME in module; use the enclosing contract and type below. | Return type of compile; see its callable contract | Module/process lifetime | 22 |
| _unique | pairs | Parameter for pairs in _unique; use the enclosing contract and type below. | list[tuple[str, Any]] | Enclosing invocation or class/instance lifetime | 25 |
| _unique | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | dict | Enclosing invocation or class/instance lifetime | 27 |
| _unique | key | Loop item for key in _unique; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 28 |
| _unique | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 28 |
| validate_json | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Any | Enclosing invocation or class/instance lifetime | 35, 49 |
| validate_json | depth | Parameter for depth in validate_json; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 35 |
| validate_json.comprehension_47 | key | Comprehension item for key in validate_json.comprehension_47; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 47 |
| validate_json | item | Loop item for item in validate_json; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 50 |
| parse_contract | text | Parameter for text in parse_contract; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 56 |
| parse_contract | contract | Validated declarative acceptance data bound to current artifact identities. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| parse_contract | exc | Caught exception for exc in parse_contract; use the enclosing contract and type below. | (RecursionError, UnicodeError) | Current exception handler; Python clears this binding afterward | 63 |
| parse_contract | seen | Local binding for seen in parse_contract; use the enclosing contract and type below. | Return type of set; see its callable contract | Enclosing invocation or class/instance lifetime | 74 |
| parse_contract | case | Loop item for case in parse_contract; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 75 |
| parse_contract.comprehension_94 | key | Comprehension item for key in parse_contract.comprehension_94; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 94 |
| parse_contract | expected | Reviewed expected observation kept outside untrusted child execution. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 98 |
| parse_contract | kind | Local binding for kind in parse_contract; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 101 |
| parse_contract.comprehension_114 | key | Comprehension item for key in parse_contract.comprehension_114; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 114 |
| _same | left | Parameter for left in _same; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 123 |
| _same | right | Parameter for right in _same; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 123 |
| _same.comprehension_128 | key | Comprehension item for key in _same.comprehension_128; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 128 |
| _same.comprehension_130 | a | Comprehension item for a in _same.comprehension_130; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 131 |
| _same.comprehension_130 | b | Comprehension item for b in _same.comprehension_130; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 131 |
| matches_expectation | observation | Parameter for observation in matches_expectation; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 136 |
| matches_expectation | expected | Reviewed expected observation kept outside untrusted child execution. | dict[str, Any] | Enclosing invocation or class/instance lifetime | 136 |
| matches_expectation | actual | Local binding for actual in matches_expectation; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 150 |
| AcceptanceEvaluator.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 168 |
| AcceptanceEvaluator.__init__ | security | Owner-scoped approval and path boundary injected into this service. | SecurityBoundary | Enclosing invocation or class/instance lifetime | 168 |
| AcceptanceEvaluator.__init__ | sandbox | Injected execution boundary; structural type alone cannot prove OS isolation. | ExecutionBackend | Enclosing invocation or class/instance lifetime | 168 |
| AcceptanceEvaluator.__init__ | ledger | Parameter for ledger in AcceptanceEvaluator.__init__; use the enclosing contract and type below. | VerificationLedger | Enclosing invocation or class/instance lifetime | 168 |
| AcceptanceEvaluator.__init__ | self.security | Owner-scoped approval and path boundary injected into this service. | tuple | Enclosing invocation or class/instance lifetime | 171 |
| AcceptanceEvaluator.__init__ | self.sandbox | Injected execution boundary; structural type alone cannot prove OS isolation. | tuple | Enclosing invocation or class/instance lifetime | 171 |
| AcceptanceEvaluator.__init__ | self.ledger | Attribute for ledger in AcceptanceEvaluator.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 171 |
| AcceptanceEvaluator.__init__ | self._lock | Attribute for lock in AcceptanceEvaluator.__init__; use the enclosing contract and type below. | Return type of RLock; see its callable contract | Enclosing invocation or class/instance lifetime | 172 |
| AcceptanceEvaluator.__init__ | self._busy | Attribute for busy in AcceptanceEvaluator.__init__; use the enclosing contract and type below. | Return type of Lock; see its callable contract | Enclosing invocation or class/instance lifetime | 173 |
| AcceptanceEvaluator.__init__ | self._status | Attribute for status in AcceptanceEvaluator.__init__; use the enclosing contract and type below. | dict[str, Any] | Enclosing invocation or class/instance lifetime | 174 |
| AcceptanceEvaluator.__init__ | self._rejected_operation | Attribute for rejected operation in AcceptanceEvaluator.__init__; use the enclosing contract and type below. | tuple[str, str] &#124; None | Enclosing invocation or class/instance lifetime | 175 |
| AcceptanceEvaluator.status | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 177 |
| AcceptanceEvaluator.status | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of deepcopy; see its callable contract | Enclosing invocation or class/instance lifetime | 180 |
| AcceptanceEvaluator.note_provisional | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 185 |
| AcceptanceEvaluator.note_provisional | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 185 |
| AcceptanceEvaluator.note_provisional | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | str | Enclosing invocation or class/instance lifetime | 185 |
| AcceptanceEvaluator._set | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 198 |
| AcceptanceEvaluator._set | stage | Parameter for stage in AcceptanceEvaluator._set; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 198 |
| AcceptanceEvaluator._set | details | Parameter for details in AcceptanceEvaluator._set; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 198 |
| AcceptanceEvaluator.submit | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 204 |
| AcceptanceEvaluator.submit | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 204 |
| AcceptanceEvaluator.submit | cases_json | Parameter for cases json in AcceptanceEvaluator.submit; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 204 |
| AcceptanceEvaluator.submit | exc | Caught exception for exc in AcceptanceEvaluator.submit; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 213 |
| AcceptanceEvaluator._submit | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 221 |
| AcceptanceEvaluator._submit | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 221 |
| AcceptanceEvaluator._submit | cases_json | Parameter for cases json in AcceptanceEvaluator._submit; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 221 |
| AcceptanceEvaluator._submit | summary | Local binding for summary in AcceptanceEvaluator._submit; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 228, 234 |
| AcceptanceEvaluator._submit | proposed | Local binding for proposed in AcceptanceEvaluator._submit; use the enclosing contract and type below. | Return type of parse_contract; see its callable contract | Enclosing invocation or class/instance lifetime | 230 |
| AcceptanceEvaluator._submit | review_text | Local binding for review text in AcceptanceEvaluator._submit; use the enclosing contract and type below. | Return type of dumps; see its callable contract | Enclosing invocation or class/instance lifetime | 231, 233 |
| AcceptanceEvaluator._submit | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 238 |
| AcceptanceEvaluator._submit | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 238 |
| AcceptanceEvaluator._submit | identity | Explicit owner identity used by a session factory or fixture. | tuple | Enclosing invocation or class/instance lifetime | 239 |
| AcceptanceEvaluator._submit | accepted | Local binding for accepted in AcceptanceEvaluator._submit; use the enclosing contract and type below. | Return type of request_user_permission; see its callable contract | Enclosing invocation or class/instance lifetime | 242 |
| AcceptanceEvaluator._submit | edited | Local binding for edited in AcceptanceEvaluator._submit; use the enclosing contract and type below. | Return type of request_user_permission; see its callable contract | Enclosing invocation or class/instance lifetime | 242 |
| AcceptanceEvaluator._submit | self._rejected_operation | Attribute for rejected operation in AcceptanceEvaluator._submit; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 254 |
| AcceptanceEvaluator._submit | approved | Local binding for approved in AcceptanceEvaluator._submit; use the enclosing contract and type below. | Return type of parse_contract; see its callable contract | Enclosing invocation or class/instance lifetime | 258 |
| AcceptanceEvaluator._submit | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of hexdigest; see its callable contract | Enclosing invocation or class/instance lifetime | 259 |
| AcceptanceEvaluator._submit | verdicts | Local binding for verdicts in AcceptanceEvaluator._submit; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 263 |
| AcceptanceEvaluator._submit | case | Loop item for case in AcceptanceEvaluator._submit; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 264 |
| AcceptanceEvaluator._submit | observed | Returned observation checked against the reviewed host-side expectation. | Return type of evaluate; see its callable contract | Enclosing invocation or class/instance lifetime | 272 |
| AcceptanceEvaluator._submit | passed | Local binding for passed in AcceptanceEvaluator._submit; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 273 |
| AcceptanceEvaluator._submit.comprehension_300 | case | Comprehension item for case in AcceptanceEvaluator._submit.comprehension_300; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 300 |
