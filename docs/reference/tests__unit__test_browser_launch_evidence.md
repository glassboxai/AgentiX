# Reference for tests/unit/test_browser_launch_evidence.py

Browser launch failures must retain bounded evidence for operator diagnosis.

Source fingerprint: 200c766cd346b2782e820d3f597e987cf8546ba6fd0501d52eeef29065d0e876

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _FailingDriver

Missing docstring: completion is blocked.

Kind: class. Declared return: Not declared / class. Source line: 10.

### _FailingDriver.__init__

Missing docstring: completion is blocked.

Kind: callable. Declared return: None. Source line: 11.

### _FailingDriver.launch

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 15.

### _OkDriver

Missing docstring: completion is blocked.

Kind: class. Declared return: Not declared / class. Source line: 19.

### _OkDriver.__init__

Missing docstring: completion is blocked.

Kind: callable. Declared return: None. Source line: 20.

### _OkDriver.launch

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 24.

### test_launch_failure_writes_bounded_evidence

A launch error retains type/detail in browser-failure.json and re-raises.

Kind: callable. Declared return: Not declared / class. Source line: 29.

### test_missing_configured_executable_fails_clearly

A configured but absent executable raises a clear actionable ValueError.

Kind: callable. Declared return: Not declared / class. Source line: 40.

### test_launch_uses_configured_executable

A valid configured executable is passed through to the driver.

Kind: callable. Declared return: Not declared / class. Source line: 47.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | launch_acceptance_browser | Imported dependency for launch acceptance browser in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| _FailingDriver.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 11 |
| _FailingDriver.__init__ | error | Parameter for error in _FailingDriver.__init__; use the enclosing contract and type below. | BaseException | Enclosing invocation or class/instance lifetime | 11 |
| _FailingDriver.__init__ | self.chromium | Attribute for chromium in _FailingDriver.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 12 |
| _FailingDriver.__init__ | self.error | Attribute for error in _FailingDriver.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 13 |
| _FailingDriver.launch | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 15 |
| _FailingDriver.launch | executable_path | Parameter for executable path in _FailingDriver.launch; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 15 |
| _OkDriver.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 20 |
| _OkDriver.__init__ | self.chromium | Attribute for chromium in _OkDriver.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 21 |
| _OkDriver.__init__ | self.seen | Attribute for seen in _OkDriver.__init__; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 22 |
| _OkDriver.launch | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 24 |
| _OkDriver.launch | executable_path | Parameter for executable path in _OkDriver.launch; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 24 |
| _OkDriver.launch | self.seen | Attribute for seen in _OkDriver.launch; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 25 |
| test_launch_failure_writes_bounded_evidence | tmp_path | Parameter for tmp path in test_launch_failure_writes_bounded_evidence; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| test_launch_failure_writes_bounded_evidence | monkeypatch | Parameter for monkeypatch in test_launch_failure_writes_bounded_evidence; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| test_launch_failure_writes_bounded_evidence | evidence | Local binding for evidence in test_launch_failure_writes_bounded_evidence; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_missing_configured_executable_fails_clearly | tmp_path | Parameter for tmp path in test_missing_configured_executable_fails_clearly; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| test_missing_configured_executable_fails_clearly | monkeypatch | Parameter for monkeypatch in test_missing_configured_executable_fails_clearly; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| test_launch_uses_configured_executable | tmp_path | Parameter for tmp path in test_launch_uses_configured_executable; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| test_launch_uses_configured_executable | monkeypatch | Parameter for monkeypatch in test_launch_uses_configured_executable; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| test_launch_uses_configured_executable | executable | Local binding for executable in test_launch_uses_configured_executable; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 49 |
| test_launch_uses_configured_executable | driver | Local binding for driver in test_launch_uses_configured_executable; use the enclosing contract and type below. | Return type of _OkDriver; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
