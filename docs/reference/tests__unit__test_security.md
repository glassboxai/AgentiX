# Reference for tests/unit/test_security.py

Characterize real storage and approval behavior without production writes.

Source fingerprint: 85c1939d0a2c30aa722ae66ea2ebedf6e41d3c55747fc6cccd22df5c15d6f779

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_resolve_valid_path

Verify resolve valid path.

Kind: callable. Declared return: Not declared / class. Source line: 12.

### test_reject_traversal

Verify reject traversal.

Kind: callable. Declared return: Not declared / class. Source line: 20.

### test_auto_approval_returns_original_content

Verify auto approval returns original content.

Kind: callable. Declared return: Not declared / class. Source line: 26.

### test_interactive_permission_round_trip

Verify interactive permission round trip.

Kind: callable. Declared return: Not declared / class. Source line: 42.

### test_interactive_permission_round_trip.respond

Provide respond for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 46.

### test_timeout_denies_and_cleans_up

Verify timeout denies and cleans up.

Kind: callable. Declared return: Not declared / class. Source line: 62.

### test_response_without_pending_request_does_nothing

Verify response without pending request does nothing.

Kind: callable. Declared return: Not declared / class. Source line: 69.

### test_real_thread_approval_handshake

Verify real thread approval handshake.

Kind: callable. Declared return: Not declared / class. Source line: 75.

### test_write_and_append_utf8

Verify write and append utf8.

Kind: callable. Declared return: Not declared / class. Source line: 100.

### test_directory_denial_leaves_no_artifacts

Verify directory denial leaves no artifacts.

Kind: callable. Declared return: Not declared / class. Source line: 108.

### test_file_denial_preserves_existing_content

Verify file denial preserves existing content.

Kind: callable. Declared return: Not declared / class. Source line: 115.

### test_edited_content_is_persisted

Verify edited content is persisted.

Kind: callable. Declared return: Not declared / class. Source line: 128.

### test_write_failure_is_reported

Verify write failure is reported.

Kind: callable. Declared return: Not declared / class. Source line: 138.

### test_reject_sibling_tool_prefix_escape

Verify reject sibling tool prefix escape.

Kind: callable. Declared return: Not declared / class. Source line: 148.

### test_reject_sibling_root_prefix_escape

Verify reject sibling root prefix escape.

Kind: callable. Declared return: Not declared / class. Source line: 154.

### test_pending_request_is_defensive_copy

Verify pending request is defensive copy.

Kind: callable. Declared return: Not declared / class. Source line: 160.

### test_reject_ambiguous_or_unsafe_windows_paths

Reject Windows aliases, traversal and drive forms before filesystem access.

Kind: callable. Declared return: Not declared / class. Source line: 190.

### test_allow_nested_relative_artifact_path

Verify allow nested relative artifact path.

Kind: callable. Declared return: Not declared / class. Source line: 196.

### test_pending_snapshot_cannot_modify_nested_state

Verify pending snapshot cannot modify nested state.

Kind: callable. Declared return: Not declared / class. Source line: 203.

### test_invalid_python_preserves_existing_file

Compilation must occur before opening/truncating the destination.

Kind: callable. Declared return: Not declared / class. Source line: 210.

### test_valid_edited_python_is_saved_without_execution

Verify valid edited python is saved without execution.

Kind: callable. Declared return: Not declared / class. Source line: 224.

### test_invalid_python_append_preserves_existing_file

Verify invalid python append preserves existing file.

Kind: callable. Declared return: Not declared / class. Source line: 235.

### test_python_alias_cannot_bypass_validation_by_resolving_to_text_file

A confined link may resolve to another suffix; the requested type still counts.

Kind: callable. Declared return: Not declared / class. Source line: 244.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| test_resolve_valid_path | system | Parameter for system in test_resolve_valid_path; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 12 |
| test_resolve_valid_path | tool | Parameter for tool in test_resolve_valid_path; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 12 |
| test_resolve_valid_path | filename | Parameter for filename in test_resolve_valid_path; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 12 |
| test_reject_traversal | system | Parameter for system in test_reject_traversal; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 20 |
| test_reject_traversal | tool | Parameter for tool in test_reject_traversal; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 20 |
| test_reject_traversal | filename | Parameter for filename in test_reject_traversal; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 20 |
| test_auto_approval_returns_original_content | system | Parameter for system in test_auto_approval_returns_original_content; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 26 |
| test_auto_approval_returns_original_content | system.security.auto_approve | Attribute for system.security.auto approve in test_auto_approval_returns_original_content; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 28 |
| test_interactive_permission_round_trip | system | Parameter for system in test_interactive_permission_round_trip; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| test_interactive_permission_round_trip | monkeypatch | Parameter for monkeypatch in test_interactive_permission_round_trip; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| test_interactive_permission_round_trip | decision | Parameter for decision in test_interactive_permission_round_trip; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| test_interactive_permission_round_trip | edited | Parameter for edited in test_interactive_permission_round_trip; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| test_interactive_permission_round_trip | expected | Reviewed expected observation kept outside untrusted child execution. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| test_interactive_permission_round_trip | sec | Local binding for sec in test_interactive_permission_round_trip; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_interactive_permission_round_trip.respond | timeout | Parameter for timeout in test_interactive_permission_round_trip.respond; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 46 |
| test_interactive_permission_round_trip.respond | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of get_pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
| test_timeout_denies_and_cleans_up | system | Parameter for system in test_timeout_denies_and_cleans_up; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 62 |
| test_timeout_denies_and_cleans_up | monkeypatch | Parameter for monkeypatch in test_timeout_denies_and_cleans_up; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 62 |
| test_timeout_denies_and_cleans_up.lambda_64 | timeout | Callback parameter for timeout in test_timeout_denies_and_cleans_up.lambda_64; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 64 |
| test_response_without_pending_request_does_nothing | system | Parameter for system in test_response_without_pending_request_does_nothing; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 69 |
| test_real_thread_approval_handshake | system | Parameter for system in test_real_thread_approval_handshake; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 75 |
| test_real_thread_approval_handshake | sec | Local binding for sec in test_real_thread_approval_handshake; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 77 |
| test_real_thread_approval_handshake | ready | Local binding for ready in test_real_thread_approval_handshake; use the enclosing contract and type below. | Return type of Event; see its callable contract | Enclosing invocation or class/instance lifetime | 78 |
| test_real_thread_approval_handshake | original_wait | Local binding for original wait in test_real_thread_approval_handshake; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 79 |
| test_real_thread_approval_handshake | sec._approval_event.wait | Attribute for sec. approval event.wait in test_real_thread_approval_handshake; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 80 |
| test_real_thread_approval_handshake.lambda_80 | timeout | Callback parameter for timeout in test_real_thread_approval_handshake.lambda_80; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 80 |
| test_real_thread_approval_handshake | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | list | Enclosing invocation or class/instance lifetime | 81 |
| test_real_thread_approval_handshake | worker | Local binding for worker in test_real_thread_approval_handshake; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| test_real_thread_approval_handshake | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of get_pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| test_write_and_append_utf8 | system | Parameter for system in test_write_and_append_utf8; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 100 |
| test_write_and_append_utf8 | system.security.auto_approve | Attribute for system.security.auto approve in test_write_and_append_utf8; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 102 |
| test_directory_denial_leaves_no_artifacts | system | Parameter for system in test_directory_denial_leaves_no_artifacts; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 108 |
| test_directory_denial_leaves_no_artifacts | monkeypatch | Parameter for monkeypatch in test_directory_denial_leaves_no_artifacts; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 108 |
| test_file_denial_preserves_existing_content | system | Parameter for system in test_file_denial_preserves_existing_content; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 115 |
| test_file_denial_preserves_existing_content | monkeypatch | Parameter for monkeypatch in test_file_denial_preserves_existing_content; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 115 |
| test_file_denial_preserves_existing_content | directory | Local binding for directory in test_file_denial_preserves_existing_content; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 117 |
| test_file_denial_preserves_existing_content | target | Local binding for target in test_file_denial_preserves_existing_content; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 119 |
| test_edited_content_is_persisted | system | Parameter for system in test_edited_content_is_persisted; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 128 |
| test_edited_content_is_persisted | monkeypatch | Parameter for monkeypatch in test_edited_content_is_persisted; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 128 |
| test_write_failure_is_reported | system | Parameter for system in test_write_failure_is_reported; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 138 |
| test_write_failure_is_reported | monkeypatch | Parameter for monkeypatch in test_write_failure_is_reported; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 138 |
| test_write_failure_is_reported | system.security.auto_approve | Attribute for system.security.auto approve in test_write_failure_is_reported; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 141 |
| test_reject_sibling_tool_prefix_escape | system | Parameter for system in test_reject_sibling_tool_prefix_escape; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 148 |
| test_reject_sibling_root_prefix_escape | system | Parameter for system in test_reject_sibling_root_prefix_escape; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 154 |
| test_pending_request_is_defensive_copy | system | Parameter for system in test_pending_request_is_defensive_copy; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 160 |
| test_pending_request_is_defensive_copy | system.security._pending_request | Attribute for system.security. pending request in test_pending_request_is_defensive_copy; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 162 |
| test_reject_ambiguous_or_unsafe_windows_paths | system | Parameter for system in test_reject_ambiguous_or_unsafe_windows_paths; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 190 |
| test_reject_ambiguous_or_unsafe_windows_paths | tool | Parameter for tool in test_reject_ambiguous_or_unsafe_windows_paths; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 190 |
| test_reject_ambiguous_or_unsafe_windows_paths | filename | Parameter for filename in test_reject_ambiguous_or_unsafe_windows_paths; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 190 |
| test_allow_nested_relative_artifact_path | system | Parameter for system in test_allow_nested_relative_artifact_path; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 196 |
| test_pending_snapshot_cannot_modify_nested_state | system | Parameter for system in test_pending_snapshot_cannot_modify_nested_state; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 203 |
| test_pending_snapshot_cannot_modify_nested_state | system.security._pending_request | Attribute for system.security. pending request in test_pending_snapshot_cannot_modify_nested_state; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 205 |
| test_invalid_python_preserves_existing_file | system | Parameter for system in test_invalid_python_preserves_existing_file; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 210 |
| test_invalid_python_preserves_existing_file | monkeypatch | Parameter for monkeypatch in test_invalid_python_preserves_existing_file; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 210 |
| test_invalid_python_preserves_existing_file | directory | Local binding for directory in test_invalid_python_preserves_existing_file; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 212 |
| test_invalid_python_preserves_existing_file | target | Local binding for target in test_invalid_python_preserves_existing_file; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 214 |
| test_invalid_python_preserves_existing_file | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of safe_write_file; see its callable contract | Enclosing invocation or class/instance lifetime | 219 |
| test_valid_edited_python_is_saved_without_execution | system | Parameter for system in test_valid_edited_python_is_saved_without_execution; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 224 |
| test_valid_edited_python_is_saved_without_execution | monkeypatch | Parameter for monkeypatch in test_valid_edited_python_is_saved_without_execution; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 224 |
| test_valid_edited_python_is_saved_without_execution | edited | Local binding for edited in test_valid_edited_python_is_saved_without_execution; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 227 |
| test_invalid_python_append_preserves_existing_file | system | Parameter for system in test_invalid_python_append_preserves_existing_file; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 235 |
| test_invalid_python_append_preserves_existing_file | system.security.auto_approve | Attribute for system.security.auto approve in test_invalid_python_append_preserves_existing_file; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 237 |
| test_invalid_python_append_preserves_existing_file | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of safe_write_file; see its callable contract | Enclosing invocation or class/instance lifetime | 239 |
| test_python_alias_cannot_bypass_validation_by_resolving_to_text_file | system | Parameter for system in test_python_alias_cannot_bypass_validation_by_resolving_to_text_file; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 244 |
| test_python_alias_cannot_bypass_validation_by_resolving_to_text_file | monkeypatch | Parameter for monkeypatch in test_python_alias_cannot_bypass_validation_by_resolving_to_text_file; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 244 |
| test_python_alias_cannot_bypass_validation_by_resolving_to_text_file | directory | Local binding for directory in test_python_alias_cannot_bypass_validation_by_resolving_to_text_file; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 246 |
| test_python_alias_cannot_bypass_validation_by_resolving_to_text_file | target | Local binding for target in test_python_alias_cannot_bypass_validation_by_resolving_to_text_file; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 248 |
| test_python_alias_cannot_bypass_validation_by_resolving_to_text_file | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of safe_write_file; see its callable contract | Enclosing invocation or class/instance lifetime | 257 |
