# Reference for tests/test_widget_style_member.py

Scoped widget styles are gated by their closed grammar, not by the app grant.

Source fingerprint: 92a553fd3e1fa17327baf8e3e728ba55501a6eacaee4fc601cd2a6205e5f4663

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_style_bytes_never_change_the_application_identity

Only executable members bind the identity; a colour edit is not a new app.

Kind: callable. Declared return: Not declared / class. Source line: 14.

### test_saved_style_keeps_the_approved_application_valid

A persisted stylesheet leaves the reviewed digest and its approval usable.

Kind: callable. Declared return: Not declared / class. Source line: 23.

### test_saved_style_rebinds_the_manifest_member_hash

Capture still proves the stylesheet on disk is the one the package declares.

Kind: callable. Declared return: Not declared / class. Source line: 37.

### test_unsafe_style_is_rejected_and_the_file_is_unchanged

The grammar, not human review, is what stops a style from moving controls.

Kind: callable. Declared return: Not declared / class. Source line: 52.

### test_style_member_rejects_a_linked_file

A hard link must not redirect a style write into an unrelated file.

Kind: callable. Declared return: Not declared / class. Source line: 69.

### test_review_style_save_keeps_the_candidate_approved

Each saved widget CSS reaches its own file without revoking approval.

Kind: callable. Declared return: Not declared / class. Source line: 85.

### test_review_code_save_still_revokes

Executable edits keep the existing revoke-before-write guarantee.

Kind: callable. Declared return: Not declared / class. Source line: 104.

### test_installed_style_write_changes_the_installed_package

A style save must reach the installed package, not only a disposable draft.

Kind: callable. Declared return: Not declared / class. Source line: 122.

### test_installed_style_write_rejects_an_unsafe_declaration

The installed package keeps its bytes when the grammar refuses the style.

Kind: callable. Declared return: Not declared / class. Source line: 148.

### test_save_file_writes_the_installed_package_for_a_style_member

The controller forwards a style save to the installed library, not only the draft.

Kind: callable. Declared return: Not declared / class. Source line: 173.

### test_save_file_writes_the_installed_package_for_a_style_member.Library

Missing docstring: completion is blocked.

Kind: class. Declared return: Not declared / class. Source line: 182.

### test_save_file_writes_the_installed_package_for_a_style_member.Library.__init__

Missing docstring: completion is blocked.

Kind: callable. Declared return: None. Source line: 183.

### test_save_file_writes_the_installed_package_for_a_style_member.Library.write_style_member

Record the installed write instead of touching a real library.

Kind: callable. Declared return: Not declared / class. Source line: 186.

### test_served_style_wins_the_preview_cascade_and_reaches_form_controls

The served copy outranks the preview sheet and styles the inner control.

Kind: callable. Declared return: Not declared / class. Source line: 223.

### test_served_style_reaches_the_caption_span_and_spares_layout_grips

The caption span is targeted directly and grips keep their own glyph size.

Kind: callable. Declared return: Not declared / class. Source line: 240.

### test_restage_styles_rewrites_the_served_stylesheet

A saved style reaches the file served to a reload and to the web tab.

Kind: callable. Declared return: Not declared / class. Source line: 255.

### test_restage_styles_preserves_successive_widget_saves

The web sheet retains every widget's latest CSS across separate saves.

Kind: callable. Declared return: Not declared / class. Source line: 281.

### test_restage_styles_keeps_the_base_stylesheet

Rebuilding the served sheet must not drop the base UI stylesheet.

Kind: callable. Declared return: Not declared / class. Source line: 310.

### test_record_sealed_with_the_legacy_digest_still_loads

An application installed before the identity change is not reported as tampered.

Kind: callable. Declared return: Not declared / class. Source line: 339.

### test_legacy_digest_does_not_accept_a_changed_member

The compatibility comparison still refuses an edited executable member.

Kind: callable. Declared return: Not declared / class. Source line: 364.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | STYLE | Module binding for STYLE in module; use the enclosing contract and type below. | str | Module/process lifetime | 10 |
| module | MEMBER | Module binding for MEMBER in module; use the enclosing contract and type below. | str | Module/process lifetime | 11 |
| test_style_bytes_never_change_the_application_identity | _identity | Imported dependency for identity in test_style_bytes_never_change_the_application_identity; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 16 |
| test_style_bytes_never_change_the_application_identity | base | Local binding for base in test_style_bytes_never_change_the_application_identity; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 18 |
| test_saved_style_keeps_the_approved_application_valid | tmp_path | Parameter for tmp path in test_saved_style_keeps_the_approved_application_valid; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 23 |
| test_saved_style_keeps_the_approved_application_valid | package | Imported dependency for package in test_saved_style_keeps_the_approved_application_valid; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 25 |
| test_saved_style_keeps_the_approved_application_valid | write_style_member | Imported dependency for write style member in test_saved_style_keeps_the_approved_application_valid; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 27 |
| test_saved_style_keeps_the_approved_application_valid | application_digest | Imported dependency for application digest in test_saved_style_keeps_the_approved_application_valid; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 28 |
| test_saved_style_keeps_the_approved_application_valid | approve_application | Imported dependency for approve application in test_saved_style_keeps_the_approved_application_valid; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 28 |
| test_saved_style_keeps_the_approved_application_valid | folder | Local binding for folder in test_saved_style_keeps_the_approved_application_valid; use the enclosing contract and type below. | Return type of package; see its callable contract | Enclosing invocation or class/instance lifetime | 30 |
| test_saved_style_keeps_the_approved_application_valid | before | Local binding for before in test_saved_style_keeps_the_approved_application_valid; use the enclosing contract and type below. | Return type of application_digest; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| test_saved_style_rebinds_the_manifest_member_hash | tmp_path | Parameter for tmp path in test_saved_style_rebinds_the_manifest_member_hash; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 37 |
| test_saved_style_rebinds_the_manifest_member_hash | package | Imported dependency for package in test_saved_style_rebinds_the_manifest_member_hash; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 39 |
| test_saved_style_rebinds_the_manifest_member_hash | capture | Imported dependency for capture in test_saved_style_rebinds_the_manifest_member_hash; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 41 |
| test_saved_style_rebinds_the_manifest_member_hash | write_style_member | Imported dependency for write style member in test_saved_style_rebinds_the_manifest_member_hash; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 42 |
| test_saved_style_rebinds_the_manifest_member_hash | folder | Local binding for folder in test_saved_style_rebinds_the_manifest_member_hash; use the enclosing contract and type below. | Return type of package; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_saved_style_rebinds_the_manifest_member_hash | files | Local binding for files in test_saved_style_rebinds_the_manifest_member_hash; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| test_saved_style_rebinds_the_manifest_member_hash | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
| test_unsafe_style_is_rejected_and_the_file_is_unchanged | tmp_path | Parameter for tmp path in test_unsafe_style_is_rejected_and_the_file_is_unchanged; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 52 |
| test_unsafe_style_is_rejected_and_the_file_is_unchanged | package | Imported dependency for package in test_unsafe_style_is_rejected_and_the_file_is_unchanged; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 54 |
| test_unsafe_style_is_rejected_and_the_file_is_unchanged | write_style_member | Imported dependency for write style member in test_unsafe_style_is_rejected_and_the_file_is_unchanged; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 56 |
| test_unsafe_style_is_rejected_and_the_file_is_unchanged | folder | Local binding for folder in test_unsafe_style_is_rejected_and_the_file_is_unchanged; use the enclosing contract and type below. | Return type of package; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| test_unsafe_style_is_rejected_and_the_file_is_unchanged | before | Local binding for before in test_unsafe_style_is_rejected_and_the_file_is_unchanged; use the enclosing contract and type below. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_style_member_rejects_a_linked_file | tmp_path | Parameter for tmp path in test_style_member_rejects_a_linked_file; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 69 |
| test_style_member_rejects_a_linked_file | package | Imported dependency for package in test_style_member_rejects_a_linked_file; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 71 |
| test_style_member_rejects_a_linked_file | write_style_member | Imported dependency for write style member in test_style_member_rejects_a_linked_file; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 73 |
| test_style_member_rejects_a_linked_file | folder | Local binding for folder in test_style_member_rejects_a_linked_file; use the enclosing contract and type below. | Return type of package; see its callable contract | Enclosing invocation or class/instance lifetime | 75 |
| test_style_member_rejects_a_linked_file | outside | Local binding for outside in test_style_member_rejects_a_linked_file; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 76 |
| test_review_style_save_keeps_the_candidate_approved | tmp_path | Parameter for tmp path in test_review_style_save_keeps_the_candidate_approved; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 85 |
| test_review_style_save_keeps_the_candidate_approved | build | Imported dependency for build in test_review_style_save_keeps_the_candidate_approved; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 87 |
| test_review_style_save_keeps_the_candidate_approved | ApplicationReview | Imported dependency for ApplicationReview in test_review_style_save_keeps_the_candidate_approved; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 89 |
| test_review_style_save_keeps_the_candidate_approved | candidate | Local binding for candidate in test_review_style_save_keeps_the_candidate_approved; use the enclosing contract and type below. | Return type of build; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| test_review_style_save_keeps_the_candidate_approved | candidate.approved | Attribute for candidate.approved in test_review_style_save_keeps_the_candidate_approved; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 92 |
| test_review_style_save_keeps_the_candidate_approved | identity | Explicit owner identity used by a session factory or fixture. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 93 |
| test_review_style_save_keeps_the_candidate_approved | vowels_member | Local binding for vowels member in test_review_style_save_keeps_the_candidate_approved; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 95 |
| test_review_style_save_keeps_the_candidate_approved | vowels_style | Local binding for vowels style in test_review_style_save_keeps_the_candidate_approved; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 96 |
| test_review_code_save_still_revokes | tmp_path | Parameter for tmp path in test_review_code_save_still_revokes; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 104 |
| test_review_code_save_still_revokes | CONNECTION_CODE | Imported dependency for CONNECTION CODE in test_review_code_save_still_revokes; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 106 |
| test_review_code_save_still_revokes | build | Imported dependency for build in test_review_code_save_still_revokes; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 106 |
| test_review_code_save_still_revokes | ApplicationReview | Imported dependency for ApplicationReview in test_review_code_save_still_revokes; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 108 |
| test_review_code_save_still_revokes | candidate | Local binding for candidate in test_review_code_save_still_revokes; use the enclosing contract and type below. | Return type of build; see its callable contract | Enclosing invocation or class/instance lifetime | 110 |
| test_review_code_save_still_revokes | candidate.approved | Attribute for candidate.approved in test_review_code_save_still_revokes; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 111 |
| test_review_code_save_still_revokes | revoked | Local binding for revoked in test_review_code_save_still_revokes; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 112 |
| test_installed_style_write_changes_the_installed_package | tmp_path | Parameter for tmp path in test_installed_style_write_changes_the_installed_package; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 122 |
| test_installed_style_write_changes_the_installed_package | make_code_candidate | Imported dependency for make code candidate in test_installed_style_write_changes_the_installed_package; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 124 |
| test_installed_style_write_changes_the_installed_package | Protector | Imported dependency for Protector in test_installed_style_write_changes_the_installed_package; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 125 |
| test_installed_style_write_changes_the_installed_package | ApplicationSupervisor | Imported dependency for ApplicationSupervisor in test_installed_style_write_changes_the_installed_package; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 127 |
| test_installed_style_write_changes_the_installed_package | InstalledApps | Imported dependency for InstalledApps in test_installed_style_write_changes_the_installed_package; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 128 |
| test_installed_style_write_changes_the_installed_package | item | Local binding for item in test_installed_style_write_changes_the_installed_package; use the enclosing contract and type below. | Return type of make_code_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| test_installed_style_write_changes_the_installed_package | item.display_name | Attribute for item.display name in test_installed_style_write_changes_the_installed_package; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 131 |
| test_installed_style_write_changes_the_installed_package | item.verified | Attribute for item.verified in test_installed_style_write_changes_the_installed_package; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 133 |
| test_installed_style_write_changes_the_installed_package | library | Local binding for library in test_installed_style_write_changes_the_installed_package; use the enclosing contract and type below. | Return type of InstalledApps; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| test_installed_style_write_changes_the_installed_package | app | Local binding for app in test_installed_style_write_changes_the_installed_package; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 135 |
| test_installed_style_write_changes_the_installed_package | member | Local binding for member in test_installed_style_write_changes_the_installed_package; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 136 |
| test_installed_style_write_changes_the_installed_package | before | Local binding for before in test_installed_style_write_changes_the_installed_package; use the enclosing contract and type below. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| test_installed_style_write_rejects_an_unsafe_declaration | tmp_path | Parameter for tmp path in test_installed_style_write_rejects_an_unsafe_declaration; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 148 |
| test_installed_style_write_rejects_an_unsafe_declaration | make_code_candidate | Imported dependency for make code candidate in test_installed_style_write_rejects_an_unsafe_declaration; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 150 |
| test_installed_style_write_rejects_an_unsafe_declaration | Protector | Imported dependency for Protector in test_installed_style_write_rejects_an_unsafe_declaration; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 151 |
| test_installed_style_write_rejects_an_unsafe_declaration | ApplicationSupervisor | Imported dependency for ApplicationSupervisor in test_installed_style_write_rejects_an_unsafe_declaration; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 153 |
| test_installed_style_write_rejects_an_unsafe_declaration | InstalledApps | Imported dependency for InstalledApps in test_installed_style_write_rejects_an_unsafe_declaration; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 154 |
| test_installed_style_write_rejects_an_unsafe_declaration | item | Local binding for item in test_installed_style_write_rejects_an_unsafe_declaration; use the enclosing contract and type below. | Return type of make_code_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 156 |
| test_installed_style_write_rejects_an_unsafe_declaration | item.display_name | Attribute for item.display name in test_installed_style_write_rejects_an_unsafe_declaration; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 157 |
| test_installed_style_write_rejects_an_unsafe_declaration | item.verified | Attribute for item.verified in test_installed_style_write_rejects_an_unsafe_declaration; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 159 |
| test_installed_style_write_rejects_an_unsafe_declaration | library | Local binding for library in test_installed_style_write_rejects_an_unsafe_declaration; use the enclosing contract and type below. | Return type of InstalledApps; see its callable contract | Enclosing invocation or class/instance lifetime | 160 |
| test_installed_style_write_rejects_an_unsafe_declaration | app | Local binding for app in test_installed_style_write_rejects_an_unsafe_declaration; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 161 |
| test_installed_style_write_rejects_an_unsafe_declaration | member | Local binding for member in test_installed_style_write_rejects_an_unsafe_declaration; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 162 |
| test_installed_style_write_rejects_an_unsafe_declaration | before | Local binding for before in test_installed_style_write_rejects_an_unsafe_declaration; use the enclosing contract and type below. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 163 |
| test_save_file_writes_the_installed_package_for_a_style_member | tmp_path | Parameter for tmp path in test_save_file_writes_the_installed_package_for_a_style_member; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 173 |
| test_save_file_writes_the_installed_package_for_a_style_member | RLock | Imported dependency for RLock in test_save_file_writes_the_installed_package_for_a_style_member; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 175 |
| test_save_file_writes_the_installed_package_for_a_style_member | build | Imported dependency for build in test_save_file_writes_the_installed_package_for_a_style_member; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 177 |
| test_save_file_writes_the_installed_package_for_a_style_member | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_save_file_writes_the_installed_package_for_a_style_member; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 179 |
| test_save_file_writes_the_installed_package_for_a_style_member | SessionRegistry | Imported dependency for SessionRegistry in test_save_file_writes_the_installed_package_for_a_style_member; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 180 |
| test_save_file_writes_the_installed_package_for_a_style_member.Library.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 183 |
| test_save_file_writes_the_installed_package_for_a_style_member.Library.__init__ | self.written | Attribute for written in test_save_file_writes_the_installed_package_for_a_style_member.Library.__init__; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 184 |
| test_save_file_writes_the_installed_package_for_a_style_member.Library.write_style_member | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 186 |
| test_save_file_writes_the_installed_package_for_a_style_member.Library.write_style_member | identity | Explicit owner identity used by a session factory or fixture. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 186 |
| test_save_file_writes_the_installed_package_for_a_style_member.Library.write_style_member | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 186 |
| test_save_file_writes_the_installed_package_for_a_style_member.Library.write_style_member | css | Parameter for css in test_save_file_writes_the_installed_package_for_a_style_member.Library.write_style_member; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 186 |
| test_save_file_writes_the_installed_package_for_a_style_member | library | Local binding for library in test_save_file_writes_the_installed_package_for_a_style_member; use the enclosing contract and type below. | Return type of Library; see its callable contract | Enclosing invocation or class/instance lifetime | 191 |
| test_save_file_writes_the_installed_package_for_a_style_member | sessions | Local binding for sessions in test_save_file_writes_the_installed_package_for_a_style_member; use the enclosing contract and type below. | Return type of SessionRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 192 |
| test_save_file_writes_the_installed_package_for_a_style_member.lambda_193 | identity | Explicit owner identity used by a session factory or fixture. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 193 |
| test_save_file_writes_the_installed_package_for_a_style_member | owner | Local binding for owner in test_save_file_writes_the_installed_package_for_a_style_member; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 200 |
| test_save_file_writes_the_installed_package_for_a_style_member | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 201 |
| test_save_file_writes_the_installed_package_for_a_style_member | _ | Local binding for  in test_save_file_writes_the_installed_package_for_a_style_member; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 202 |
| test_save_file_writes_the_installed_package_for_a_style_member | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 202 |
| test_save_file_writes_the_installed_package_for_a_style_member | candidate | Local binding for candidate in test_save_file_writes_the_installed_package_for_a_style_member; use the enclosing contract and type below. | Return type of build; see its callable contract | Enclosing invocation or class/instance lifetime | 203 |
| test_save_file_writes_the_installed_package_for_a_style_member | candidate.catalog_id | Attribute for candidate.catalog id in test_save_file_writes_the_installed_package_for_a_style_member; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 204 |
| test_save_file_writes_the_installed_package_for_a_style_member | state.candidate | Attribute for state.candidate in test_save_file_writes_the_installed_package_for_a_style_member; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 205 |
| test_save_file_writes_the_installed_package_for_a_style_member | message | Local binding for message in test_save_file_writes_the_installed_package_for_a_style_member; use the enclosing contract and type below. | Return type of save_file; see its callable contract | Enclosing invocation or class/instance lifetime | 206 |
| test_served_style_wins_the_preview_cascade_and_reaches_form_controls | served_style | Imported dependency for served style in test_served_style_wins_the_preview_cascade_and_reaches_form_controls; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 225 |
| test_served_style_wins_the_preview_cascade_and_reaches_form_controls | css | Local binding for css in test_served_style_wins_the_preview_cascade_and_reaches_form_controls; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 227 |
| test_served_style_wins_the_preview_cascade_and_reaches_form_controls | served | Local binding for served in test_served_style_wins_the_preview_cascade_and_reaches_form_controls; use the enclosing contract and type below. | Return type of decode; see its callable contract | Enclosing invocation or class/instance lifetime | 231 |
| test_served_style_reaches_the_caption_span_and_spares_layout_grips | served_style | Imported dependency for served style in test_served_style_reaches_the_caption_span_and_spares_layout_grips; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 242 |
| test_served_style_reaches_the_caption_span_and_spares_layout_grips | css | Local binding for css in test_served_style_reaches_the_caption_span_and_spares_layout_grips; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 244 |
| test_served_style_reaches_the_caption_span_and_spares_layout_grips | served | Local binding for served in test_served_style_reaches_the_caption_span_and_spares_layout_grips; use the enclosing contract and type below. | Return type of decode; see its callable contract | Enclosing invocation or class/instance lifetime | 248 |
| test_restage_styles_rewrites_the_served_stylesheet | tmp_path | Parameter for tmp path in test_restage_styles_rewrites_the_served_stylesheet; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 255 |
| test_restage_styles_rewrites_the_served_stylesheet | package | Imported dependency for package in test_restage_styles_rewrites_the_served_stylesheet; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 257 |
| test_restage_styles_rewrites_the_served_stylesheet | capture | Imported dependency for capture in test_restage_styles_rewrites_the_served_stylesheet; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 259 |
| test_restage_styles_rewrites_the_served_stylesheet | ApplicationSession | Imported dependency for ApplicationSession in test_restage_styles_rewrites_the_served_stylesheet; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 260 |
| test_restage_styles_rewrites_the_served_stylesheet | folder | Local binding for folder in test_restage_styles_rewrites_the_served_stylesheet; use the enclosing contract and type below. | Return type of package; see its callable contract | Enclosing invocation or class/instance lifetime | 262 |
| test_restage_styles_rewrites_the_served_stylesheet | files | Local binding for files in test_restage_styles_rewrites_the_served_stylesheet; use the enclosing contract and type below. | Return type of capture; see its callable contract | Enclosing invocation or class/instance lifetime | 263 |
| test_restage_styles_rewrites_the_served_stylesheet | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 264 |
| test_restage_styles_rewrites_the_served_stylesheet | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 265 |
| test_restage_styles_rewrites_the_served_stylesheet | session | Local binding for session in test_restage_styles_rewrites_the_served_stylesheet; use the enclosing contract and type below. | Return type of __new__; see its callable contract | Enclosing invocation or class/instance lifetime | 268 |
| test_restage_styles_rewrites_the_served_stylesheet | session.root | Attribute for session.root in test_restage_styles_rewrites_the_served_stylesheet; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 269 |
| test_restage_styles_rewrites_the_served_stylesheet | session.application | Attribute for session.application in test_restage_styles_rewrites_the_served_stylesheet; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 270 |
| test_restage_styles_rewrites_the_served_stylesheet | session.manifest | Attribute for session.manifest in test_restage_styles_rewrites_the_served_stylesheet; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 271 |
| test_restage_styles_rewrites_the_served_stylesheet | served | Local binding for served in test_restage_styles_rewrites_the_served_stylesheet; use the enclosing contract and type below. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 276 |
| test_restage_styles_preserves_successive_widget_saves | tmp_path | Parameter for tmp path in test_restage_styles_preserves_successive_widget_saves; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 281 |
| test_restage_styles_preserves_successive_widget_saves | package | Imported dependency for package in test_restage_styles_preserves_successive_widget_saves; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 283 |
| test_restage_styles_preserves_successive_widget_saves | capture | Imported dependency for capture in test_restage_styles_preserves_successive_widget_saves; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 285 |
| test_restage_styles_preserves_successive_widget_saves | ApplicationSession | Imported dependency for ApplicationSession in test_restage_styles_preserves_successive_widget_saves; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 286 |
| test_restage_styles_preserves_successive_widget_saves | files | Local binding for files in test_restage_styles_preserves_successive_widget_saves; use the enclosing contract and type below. | Return type of capture; see its callable contract | Enclosing invocation or class/instance lifetime | 288 |
| test_restage_styles_preserves_successive_widget_saves | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 289 |
| test_restage_styles_preserves_successive_widget_saves | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 290 |
| test_restage_styles_preserves_successive_widget_saves | session | Local binding for session in test_restage_styles_preserves_successive_widget_saves; use the enclosing contract and type below. | Return type of __new__; see its callable contract | Enclosing invocation or class/instance lifetime | 293 |
| test_restage_styles_preserves_successive_widget_saves | session.root | Attribute for session.root in test_restage_styles_preserves_successive_widget_saves; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 294 |
| test_restage_styles_preserves_successive_widget_saves | session.application | Attribute for session.application in test_restage_styles_preserves_successive_widget_saves; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 295 |
| test_restage_styles_preserves_successive_widget_saves | session.manifest | Attribute for session.manifest in test_restage_styles_preserves_successive_widget_saves; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 296 |
| test_restage_styles_preserves_successive_widget_saves | served | Local binding for served in test_restage_styles_preserves_successive_widget_saves; use the enclosing contract and type below. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 305 |
| test_restage_styles_keeps_the_base_stylesheet | tmp_path | Parameter for tmp path in test_restage_styles_keeps_the_base_stylesheet; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 310 |
| test_restage_styles_keeps_the_base_stylesheet | package | Imported dependency for package in test_restage_styles_keeps_the_base_stylesheet; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 312 |
| test_restage_styles_keeps_the_base_stylesheet | capture | Imported dependency for capture in test_restage_styles_keeps_the_base_stylesheet; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 314 |
| test_restage_styles_keeps_the_base_stylesheet | STYLE_MARKER | Imported dependency for STYLE MARKER in test_restage_styles_keeps_the_base_stylesheet; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 315 |
| test_restage_styles_keeps_the_base_stylesheet | ApplicationSession | Imported dependency for ApplicationSession in test_restage_styles_keeps_the_base_stylesheet; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 315 |
| test_restage_styles_keeps_the_base_stylesheet | folder | Local binding for folder in test_restage_styles_keeps_the_base_stylesheet; use the enclosing contract and type below. | Return type of package; see its callable contract | Enclosing invocation or class/instance lifetime | 317 |
| test_restage_styles_keeps_the_base_stylesheet | files | Local binding for files in test_restage_styles_keeps_the_base_stylesheet; use the enclosing contract and type below. | Return type of capture; see its callable contract | Enclosing invocation or class/instance lifetime | 318 |
| test_restage_styles_keeps_the_base_stylesheet | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 319 |
| test_restage_styles_keeps_the_base_stylesheet | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 320 |
| test_restage_styles_keeps_the_base_stylesheet | base | Local binding for base in test_restage_styles_keeps_the_base_stylesheet; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 322 |
| test_restage_styles_keeps_the_base_stylesheet | session | Local binding for session in test_restage_styles_keeps_the_base_stylesheet; use the enclosing contract and type below. | Return type of __new__; see its callable contract | Enclosing invocation or class/instance lifetime | 324 |
| test_restage_styles_keeps_the_base_stylesheet | session.root | Attribute for session.root in test_restage_styles_keeps_the_base_stylesheet; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 325 |
| test_restage_styles_keeps_the_base_stylesheet | session.application | Attribute for session.application in test_restage_styles_keeps_the_base_stylesheet; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 326 |
| test_restage_styles_keeps_the_base_stylesheet | session.manifest | Attribute for session.manifest in test_restage_styles_keeps_the_base_stylesheet; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 327 |
| test_restage_styles_keeps_the_base_stylesheet | served | Local binding for served in test_restage_styles_keeps_the_base_stylesheet; use the enclosing contract and type below. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 332 |
| test_record_sealed_with_the_legacy_digest_still_loads | tmp_path | Parameter for tmp path in test_record_sealed_with_the_legacy_digest_still_loads; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 339 |
| test_record_sealed_with_the_legacy_digest_still_loads | json | Imported dependency for json in test_record_sealed_with_the_legacy_digest_still_loads; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 341 |
| test_record_sealed_with_the_legacy_digest_still_loads | make_code_candidate | Imported dependency for make code candidate in test_record_sealed_with_the_legacy_digest_still_loads; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 343 |
| test_record_sealed_with_the_legacy_digest_still_loads | Protector | Imported dependency for Protector in test_record_sealed_with_the_legacy_digest_still_loads; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 344 |
| test_record_sealed_with_the_legacy_digest_still_loads | ApplicationSupervisor | Imported dependency for ApplicationSupervisor in test_record_sealed_with_the_legacy_digest_still_loads; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 346 |
| test_record_sealed_with_the_legacy_digest_still_loads | application_digest | Imported dependency for application digest in test_record_sealed_with_the_legacy_digest_still_loads; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 347 |
| test_record_sealed_with_the_legacy_digest_still_loads | InstalledApps | Imported dependency for InstalledApps in test_record_sealed_with_the_legacy_digest_still_loads; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 348 |
| test_record_sealed_with_the_legacy_digest_still_loads | _legacy_digest | Imported dependency for legacy digest in test_record_sealed_with_the_legacy_digest_still_loads; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 348 |
| test_record_sealed_with_the_legacy_digest_still_loads | item | Local binding for item in test_record_sealed_with_the_legacy_digest_still_loads; use the enclosing contract and type below. | Return type of make_code_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 350 |
| test_record_sealed_with_the_legacy_digest_still_loads | item.display_name | Attribute for item.display name in test_record_sealed_with_the_legacy_digest_still_loads; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 351 |
| test_record_sealed_with_the_legacy_digest_still_loads | item.verified | Attribute for item.verified in test_record_sealed_with_the_legacy_digest_still_loads; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 353 |
| test_record_sealed_with_the_legacy_digest_still_loads | library | Local binding for library in test_record_sealed_with_the_legacy_digest_still_loads; use the enclosing contract and type below. | Return type of InstalledApps; see its callable contract | Enclosing invocation or class/instance lifetime | 354 |
| test_record_sealed_with_the_legacy_digest_still_loads | installed | Local binding for installed in test_record_sealed_with_the_legacy_digest_still_loads; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 355 |
| test_record_sealed_with_the_legacy_digest_still_loads | record_path | Local binding for record path in test_record_sealed_with_the_legacy_digest_still_loads; use the enclosing contract and type below. | Return type of _record; see its callable contract | Enclosing invocation or class/instance lifetime | 357 |
| test_record_sealed_with_the_legacy_digest_still_loads | record | Local binding for record in test_record_sealed_with_the_legacy_digest_still_loads; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 358 |
| test_legacy_digest_does_not_accept_a_changed_member | tmp_path | Parameter for tmp path in test_legacy_digest_does_not_accept_a_changed_member; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 364 |
| test_legacy_digest_does_not_accept_a_changed_member | json | Imported dependency for json in test_legacy_digest_does_not_accept_a_changed_member; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 366 |
| test_legacy_digest_does_not_accept_a_changed_member | make_code_candidate | Imported dependency for make code candidate in test_legacy_digest_does_not_accept_a_changed_member; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 368 |
| test_legacy_digest_does_not_accept_a_changed_member | Protector | Imported dependency for Protector in test_legacy_digest_does_not_accept_a_changed_member; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 369 |
| test_legacy_digest_does_not_accept_a_changed_member | ApplicationSupervisor | Imported dependency for ApplicationSupervisor in test_legacy_digest_does_not_accept_a_changed_member; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 371 |
| test_legacy_digest_does_not_accept_a_changed_member | InstalledApps | Imported dependency for InstalledApps in test_legacy_digest_does_not_accept_a_changed_member; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 372 |
| test_legacy_digest_does_not_accept_a_changed_member | _legacy_digest | Imported dependency for legacy digest in test_legacy_digest_does_not_accept_a_changed_member; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 372 |
| test_legacy_digest_does_not_accept_a_changed_member | item | Local binding for item in test_legacy_digest_does_not_accept_a_changed_member; use the enclosing contract and type below. | Return type of make_code_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 374 |
| test_legacy_digest_does_not_accept_a_changed_member | item.display_name | Attribute for item.display name in test_legacy_digest_does_not_accept_a_changed_member; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 375 |
| test_legacy_digest_does_not_accept_a_changed_member | item.verified | Attribute for item.verified in test_legacy_digest_does_not_accept_a_changed_member; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 377 |
| test_legacy_digest_does_not_accept_a_changed_member | library | Local binding for library in test_legacy_digest_does_not_accept_a_changed_member; use the enclosing contract and type below. | Return type of InstalledApps; see its callable contract | Enclosing invocation or class/instance lifetime | 378 |
| test_legacy_digest_does_not_accept_a_changed_member | installed | Local binding for installed in test_legacy_digest_does_not_accept_a_changed_member; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 379 |
| test_legacy_digest_does_not_accept_a_changed_member | record_path | Local binding for record path in test_legacy_digest_does_not_accept_a_changed_member; use the enclosing contract and type below. | Return type of _record; see its callable contract | Enclosing invocation or class/instance lifetime | 380 |
| test_legacy_digest_does_not_accept_a_changed_member | record | Local binding for record in test_legacy_digest_does_not_accept_a_changed_member; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 381 |
