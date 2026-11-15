# Reference for tests/unit/test_catalog_actions_front.py

Catalog action controls: selection pre-checks must open the modal dialog.

Source fingerprint: fccfbf5560039151b2f462a5a1b66aef2f96570e0e37faf1a2d7c10ed91e28a4

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _fake_gr

Record constructor kwargs and capture every event binding's fn.

Kind: callable. Declared return: Not declared / class. Source line: 8.

### _fake_gr.Component

Absorb constructor kwargs and record event registrations.

Kind: class. Declared return: Not declared / class. Source line: 11.

### _fake_gr.Component.__init__

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 14.

### _fake_gr.Component.__enter__

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 17.

### _fake_gr.Component.__exit__

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 20.

### _fake_gr.Component.__getattr__

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 23.

### _fake_gr.Component.__getattr__.event

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 24.

### _DialogStub

Record modal requests without building real components.

Kind: class. Declared return: Not declared / class. Source line: 36.

### _DialogStub.__init__

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 39.

### _DialogStub.outputs

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 42.

### _DialogStub.skip

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 45.

### _DialogStub.show

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 48.

### test_delete_prepare_requires_selection_and_opens_modal

Deletion with no selection shows the friendly modal before any backend call.

Kind: callable. Declared return: Not declared / class. Source line: 53.

### test_delete_prepare_requires_selection_and_opens_modal.Backend

Fail loudly if the backend is reached without a selection.

Kind: class. Declared return: Not declared / class. Source line: 60.

### test_delete_prepare_requires_selection_and_opens_modal.Backend.prepare

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 63.

### test_delete_backend_errors_open_the_modal_with_the_safe_message

Backend validation and unexpected failures open the modal, not a toast.

Kind: callable. Declared return: Not declared / class. Source line: 76.

### test_delete_backend_errors_open_the_modal_with_the_safe_message.Backend

Raise one validation error and one unexpected error.

Kind: class. Declared return: Not declared / class. Source line: 83.

### test_delete_backend_errors_open_the_modal_with_the_safe_message.Backend.prepare

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 86.

### test_delete_success_leaves_the_modal_hidden

A successful prepare keeps the dialog outputs untouched.

Kind: callable. Declared return: Not declared / class. Source line: 102.

### test_delete_success_leaves_the_modal_hidden.Backend

Return a normal confirmation prompt.

Kind: class. Declared return: Not declared / class. Source line: 109.

### test_delete_success_leaves_the_modal_hidden.Backend.prepare

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 112.

### test_load_and_play_reject_empty_selection_before_backend

The catalog pre-check raises the friendly validation message.

Kind: callable. Declared return: Not declared / class. Source line: 130.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| _fake_gr | events | Parameter for events in _fake_gr; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 8 |
| _fake_gr.Component.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| _fake_gr.Component.__init__ | args | Parameter for args in _fake_gr.Component.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| _fake_gr.Component.__init__ | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| _fake_gr.Component.__init__ | self.kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 15 |
| _fake_gr.Component.__enter__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 17 |
| _fake_gr.Component.__exit__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 20 |
| _fake_gr.Component.__exit__ | args | Parameter for args in _fake_gr.Component.__exit__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 20 |
| _fake_gr.Component.__getattr__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 23 |
| _fake_gr.Component.__getattr__ | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 23 |
| _fake_gr.Component.__getattr__.event | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 24 |
| _fake_gr.comprehension_31 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 31 |
| _DialogStub.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 39 |
| _DialogStub.__init__ | self.shown | Attribute for shown in _DialogStub.__init__; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 40 |
| _DialogStub.outputs | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| _DialogStub.skip | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 45 |
| _DialogStub.show | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 48 |
| _DialogStub.show | text | Parameter for text in _DialogStub.show; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 48 |
| test_delete_prepare_requires_selection_and_opens_modal | build_delete_controls | Imported dependency for build delete controls in test_delete_prepare_requires_selection_and_opens_modal; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 55 |
| test_delete_prepare_requires_selection_and_opens_modal | events | Local binding for events in test_delete_prepare_requires_selection_and_opens_modal; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 57 |
| test_delete_prepare_requires_selection_and_opens_modal | dialog | Local binding for dialog in test_delete_prepare_requires_selection_and_opens_modal; use the enclosing contract and type below. | Return type of _DialogStub; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| test_delete_prepare_requires_selection_and_opens_modal.Backend.prepare | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| test_delete_prepare_requires_selection_and_opens_modal.Backend.prepare | kind | Parameter for kind in test_delete_prepare_requires_selection_and_opens_modal.Backend.prepare; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| test_delete_prepare_requires_selection_and_opens_modal.Backend.prepare | identity | Explicit owner identity used by a session factory or fixture. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| test_delete_prepare_requires_selection_and_opens_modal.Backend.prepare | token | Parameter for token in test_delete_prepare_requires_selection_and_opens_modal.Backend.prepare; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| test_delete_prepare_requires_selection_and_opens_modal.Backend.prepare | request | Parameter for request in test_delete_prepare_requires_selection_and_opens_modal.Backend.prepare; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| test_delete_prepare_requires_selection_and_opens_modal.lambda_67 | fn | Callback parameter for fn in test_delete_prepare_requires_selection_and_opens_modal.lambda_67; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 67 |
| test_delete_prepare_requires_selection_and_opens_modal | prepare | Local binding for prepare in test_delete_prepare_requires_selection_and_opens_modal; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 69 |
| test_delete_prepare_requires_selection_and_opens_modal | row | Local binding for row in test_delete_prepare_requires_selection_and_opens_modal; use the enclosing contract and type below. | Return type of prepare; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_delete_backend_errors_open_the_modal_with_the_safe_message | build_delete_controls | Imported dependency for build delete controls in test_delete_backend_errors_open_the_modal_with_the_safe_message; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 78 |
| test_delete_backend_errors_open_the_modal_with_the_safe_message | events | Local binding for events in test_delete_backend_errors_open_the_modal_with_the_safe_message; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 80 |
| test_delete_backend_errors_open_the_modal_with_the_safe_message | dialog | Local binding for dialog in test_delete_backend_errors_open_the_modal_with_the_safe_message; use the enclosing contract and type below. | Return type of _DialogStub; see its callable contract | Enclosing invocation or class/instance lifetime | 81 |
| test_delete_backend_errors_open_the_modal_with_the_safe_message.Backend.prepare | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 86 |
| test_delete_backend_errors_open_the_modal_with_the_safe_message.Backend.prepare | kind | Parameter for kind in test_delete_backend_errors_open_the_modal_with_the_safe_message.Backend.prepare; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 86 |
| test_delete_backend_errors_open_the_modal_with_the_safe_message.Backend.prepare | identity | Explicit owner identity used by a session factory or fixture. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 86 |
| test_delete_backend_errors_open_the_modal_with_the_safe_message.Backend.prepare | token | Parameter for token in test_delete_backend_errors_open_the_modal_with_the_safe_message.Backend.prepare; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 86 |
| test_delete_backend_errors_open_the_modal_with_the_safe_message.Backend.prepare | request | Parameter for request in test_delete_backend_errors_open_the_modal_with_the_safe_message.Backend.prepare; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 86 |
| test_delete_backend_errors_open_the_modal_with_the_safe_message.lambda_92 | fn | Callback parameter for fn in test_delete_backend_errors_open_the_modal_with_the_safe_message.lambda_92; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 92 |
| test_delete_backend_errors_open_the_modal_with_the_safe_message | prepare | Local binding for prepare in test_delete_backend_errors_open_the_modal_with_the_safe_message; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 94 |
| test_delete_backend_errors_open_the_modal_with_the_safe_message | row | Local binding for row in test_delete_backend_errors_open_the_modal_with_the_safe_message; use the enclosing contract and type below. | Return type of prepare; see its callable contract | Enclosing invocation or class/instance lifetime | 95, 98 |
| test_delete_success_leaves_the_modal_hidden | build_delete_controls | Imported dependency for build delete controls in test_delete_success_leaves_the_modal_hidden; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 104 |
| test_delete_success_leaves_the_modal_hidden | events | Local binding for events in test_delete_success_leaves_the_modal_hidden; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 106 |
| test_delete_success_leaves_the_modal_hidden | dialog | Local binding for dialog in test_delete_success_leaves_the_modal_hidden; use the enclosing contract and type below. | Return type of _DialogStub; see its callable contract | Enclosing invocation or class/instance lifetime | 107 |
| test_delete_success_leaves_the_modal_hidden.Backend.prepare | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 112 |
| test_delete_success_leaves_the_modal_hidden.Backend.prepare | kind | Parameter for kind in test_delete_success_leaves_the_modal_hidden.Backend.prepare; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 112 |
| test_delete_success_leaves_the_modal_hidden.Backend.prepare | identity | Explicit owner identity used by a session factory or fixture. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 112 |
| test_delete_success_leaves_the_modal_hidden.Backend.prepare | token | Parameter for token in test_delete_success_leaves_the_modal_hidden.Backend.prepare; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 112 |
| test_delete_success_leaves_the_modal_hidden.Backend.prepare | request | Parameter for request in test_delete_success_leaves_the_modal_hidden.Backend.prepare; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 112 |
| test_delete_success_leaves_the_modal_hidden.lambda_116 | fn | Callback parameter for fn in test_delete_success_leaves_the_modal_hidden.lambda_116; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 116 |
| test_delete_success_leaves_the_modal_hidden | prepare | Local binding for prepare in test_delete_success_leaves_the_modal_hidden; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 118 |
| test_delete_success_leaves_the_modal_hidden | row | Local binding for row in test_delete_success_leaves_the_modal_hidden; use the enclosing contract and type below. | Return type of prepare; see its callable contract | Enclosing invocation or class/instance lifetime | 119 |
| test_load_and_play_reject_empty_selection_before_backend | require_selected_app | Imported dependency for require selected app in test_load_and_play_reject_empty_selection_before_backend; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 132 |
