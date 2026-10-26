# Reference for tests/integration/test_live_review_ui_contract.py

LIVE-UI-001: no-output Gradio callbacks must not return ignored values.

Source fingerprint: c6bd20955dd5a9737ee65ad11c5e47bf012ebe407159940d33efbdc336aee99b

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_approval_callback_respects_real_gradio_output_contract

Exercise the registered callback rather than matching its source text.

Kind: callable. Declared return: Not declared / class. Source line: 11.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| test_approval_callback_respects_real_gradio_output_contract | script | Local binding for script in test_approval_callback_respects_real_gradio_output_contract; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 13 |
| test_approval_callback_respects_real_gradio_output_contract | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
