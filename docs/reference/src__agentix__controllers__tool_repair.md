# Reference for src/agentix/controllers/tool_repair.py

Session-owned rejected-tool editor and explicit validation restart controller.

Source fingerprint: dd605dd937a576315d790d760526e0baa68a25288bfda2d31279a034974be5bb

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ToolRepairBackend

Bind editable buffers to the exact rejected proposal loaded by this browser.

Kind: class. Declared return: Not declared / class. Source line: 11.

### ToolRepairBackend.__init__

Inject the application dependency library and acceptance proposal service.

Kind: callable. Declared return: Not declared / class. Source line: 14.

### ToolRepairBackend._idle

Require the rejected workflow to finish before a new explicit repair.

Kind: callable. Declared return: None. Source line: 20.

### ToolRepairBackend.load

Return only this owner's retained rejected buffers and a fresh editor nonce.

Kind: callable. Declared return: Not declared / class. Source line: 28.

### ToolRepairBackend.resume

Start a new bounded owner operation, never a continuation of denied approval.

Kind: callable. Declared return: Not declared / class. Source line: 45.

### ToolRepairBackend.resume.saved

Keep corrected buffers available after a failure or another rejection.

Kind: callable. Declared return: Not declared / class. Source line: 62.

### ToolRepairBackend.resume.operation

Reuse the controller's synchronized worker, activity capture and status.

Kind: callable. Declared return: Not declared / class. Source line: 77.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | secrets | Imported dependency for secrets in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | propose_repair_cases | Imported dependency for propose repair cases in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | ToolRepair | Imported dependency for ToolRepair in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | SessionOwnerAccess | Imported dependency for SessionOwnerAccess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| ToolRepairBackend.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| ToolRepairBackend.__init__ | registry | Parameter for registry in ToolRepairBackend.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| ToolRepairBackend.__init__ | applications | Parameter for applications in ToolRepairBackend.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| ToolRepairBackend.__init__ | proposer | Parameter for proposer in ToolRepairBackend.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| ToolRepairBackend.__init__ | self.applications | Attribute for applications in ToolRepairBackend.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 17 |
| ToolRepairBackend.__init__ | self.proposer | Attribute for proposer in ToolRepairBackend.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 17 |
| ToolRepairBackend._idle | controller | Parameter for controller in ToolRepairBackend._idle; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 20 |
| ToolRepairBackend._idle.comprehension_22 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 24 |
| ToolRepairBackend.load | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 28 |
| ToolRepairBackend.load | token | Parameter for token in ToolRepairBackend.load; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 28 |
| ToolRepairBackend.load | request | Parameter for request in ToolRepairBackend.load; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 28 |
| ToolRepairBackend.load | session | Local binding for session in ToolRepairBackend.load; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 30 |
| ToolRepairBackend.load | draft | Local binding for draft in ToolRepairBackend.load; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| ToolRepairBackend.load | revision | Local binding for revision in ToolRepairBackend.load; use the enclosing contract and type below. | Return type of token_urlsafe; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| ToolRepairBackend.load | session.controller._repair_loaded | Attribute for session.controller. repair loaded in ToolRepairBackend.load; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 37 |
| ToolRepairBackend.load | hint | Local binding for hint in ToolRepairBackend.load; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 38, 42 |
| ToolRepairBackend.resume | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 45 |
| ToolRepairBackend.resume | revision | Parameter for revision in ToolRepairBackend.resume; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 45 |
| ToolRepairBackend.resume | code | Source snapshot passed through approval, syntax checks and isolated staging. | str | Enclosing invocation or class/instance lifetime | 45 |
| ToolRepairBackend.resume | tests | Optional unittest source snapshot; child-authored success remains provisional. | str | Enclosing invocation or class/instance lifetime | 45 |
| ToolRepairBackend.resume | token | Parameter for token in ToolRepairBackend.resume; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 45 |
| ToolRepairBackend.resume | request | Parameter for request in ToolRepairBackend.resume; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 45 |
| ToolRepairBackend.resume | session | Local binding for session in ToolRepairBackend.resume; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| ToolRepairBackend.resume | controller | Local binding for controller in ToolRepairBackend.resume; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 48 |
| ToolRepairBackend.resume | loaded | Local binding for loaded in ToolRepairBackend.resume; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| ToolRepairBackend.resume | controller._repair_loaded | Attribute for controller. repair loaded in ToolRepairBackend.resume; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 59 |
| ToolRepairBackend.resume | draft | Local binding for draft in ToolRepairBackend.resume; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 60 |
| ToolRepairBackend.resume.saved | current | Parameter for current in ToolRepairBackend.resume.saved; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 62 |
| ToolRepairBackend.resume.saved | controller._rejected_tool | Attribute for controller. rejected tool in ToolRepairBackend.resume.saved; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 65 |
| ToolRepairBackend.resume | service | Local binding for service in ToolRepairBackend.resume; use the enclosing contract and type below. | Return type of ToolRepair; see its callable contract | Enclosing invocation or class/instance lifetime | 67 |
| ToolRepairBackend.resume.lambda_71 | context | Callback parameter for context in ToolRepairBackend.resume.lambda_71; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 71 |
| ToolRepairBackend.resume.operation | query | Original user request or a trusted test query; avoid payload logging by default. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 77 |
| ToolRepairBackend.resume.operation | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of save_and_validate; see its callable contract | Enclosing invocation or class/instance lifetime | 79 |
| ToolRepairBackend.resume.operation | controller._rejected_tool | Attribute for controller. rejected tool in ToolRepairBackend.resume.operation; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 82 |
| ToolRepairBackend.resume.operation | observed | Returned observation checked against the reviewed host-side expectation. | Return type of execution_result; see its callable contract | Enclosing invocation or class/instance lifetime | 83 |
