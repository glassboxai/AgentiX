# Reference for tests/test_widget_style_editor.py

The widget style window edits six declarations and preserves everything else.

Source fingerprint: 0851a3bfe17516da9d0890c90a559153b87199aaaea9891beb48b7330dfdcbff

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_defaults_are_read_from_the_generated_palette

A freshly generated stylesheet opens on documented defaults.

Kind: callable. Declared return: Not declared / class. Source line: 12.

### test_merge_preserves_unmanaged_declarations_and_hover_blocks

Only the six managed declarations change; the rest of the file survives.

Kind: callable. Declared return: Not declared / class. Source line: 25.

### test_zero_width_never_draws_a_border

A zero width derives ``none`` so the stored file matches what is shown.

Kind: callable. Declared return: Not declared / class. Source line: 45.

### test_merge_creates_the_base_block_when_only_hover_exists

A hover-only file still receives the editable block in front.

Kind: callable. Declared return: Not declared / class. Source line: 58.

### test_round_trip_returns_the_saved_values

What the window saves is what the window reads back.

Kind: callable. Declared return: Not declared / class. Source line: 71.

### test_field_and_caption_values_round_trip

The field box and the caption keep their own colour, family and size.

Kind: callable. Declared return: Not declared / class. Source line: 81.

### test_merge_preserves_unmanaged_field_declarations

A padding already present on the field block survives the rewrite.

Kind: callable. Declared return: Not declared / class. Source line: 94.

### test_repeated_saves_never_accumulate_duplicate_blocks

A second save replaces the owned blocks instead of appending new ones.

Kind: callable. Declared return: Not declared / class. Source line: 108.

### test_field_and_caption_defaults_are_read_from_a_plain_file

A file without inner blocks opens on documented defaults.

Kind: callable. Declared return: Not declared / class. Source line: 122.

### test_out_of_range_values_are_rejected

Bounds are enforced before the grammar sees a declaration.

Kind: callable. Declared return: Not declared / class. Source line: 145.

### _Applications

Minimal double: only the two calls the style backend may make.

Kind: class. Declared return: Not declared / class. Source line: 154.

### _Applications.__init__

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 157.

### _Applications.owned_candidate

Return the fixture proposal without any session registry.

Kind: callable. Declared return: Not declared / class. Source line: 161.

### _Applications.save_file

Record the persisted member instead of touching a real review.

Kind: callable. Declared return: Not declared / class. Source line: 165.

### test_backend_load_returns_the_window_values

The window opens on the stored declarations of the right-clicked widget.

Kind: callable. Declared return: Not declared / class. Source line: 171.

### test_backend_save_persists_the_merged_stylesheet

Saving delegates to the review service with the merged member text.

Kind: callable. Declared return: Not declared / class. Source line: 193.

### test_backend_payload_carries_the_widget_instance_ids

The live preview scopes CSS to instance ids, not to the tool role.

Kind: callable. Declared return: Not declared / class. Source line: 214.

### test_backend_rejects_an_unknown_widget

Browser text never becomes a path or an arbitrary member name.

Kind: callable. Declared return: Not declared / class. Source line: 227.

### test_save_closes_the_window_on_success

A successful save hides the overlay instead of leaving it open.

Kind: callable. Declared return: Not declared / class. Source line: 237.

### test_save_keeps_the_window_open_when_a_value_is_rejected

A rejected value raises before any close update is produced.

Kind: callable. Declared return: Not declared / class. Source line: 254.

### test_save_keeps_the_window_open_when_a_value_is_rejected.reject

Refuse the write the way the review service does.

Kind: callable. Declared return: Not declared / class. Source line: 258.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | ROLE | Module binding for ROLE in module; use the enclosing contract and type below. | str | Module/process lifetime | 8 |
| module | SELECTOR | Module binding for SELECTOR in module; use the enclosing contract and type below. | str | Module/process lifetime | 9 |
| test_defaults_are_read_from_the_generated_palette | read_style | Imported dependency for read style in test_defaults_are_read_from_the_generated_palette; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 14 |
| test_defaults_are_read_from_the_generated_palette | default_widget_css | Imported dependency for default widget css in test_defaults_are_read_from_the_generated_palette; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 15 |
| test_defaults_are_read_from_the_generated_palette | values | Local binding for values in test_defaults_are_read_from_the_generated_palette; use the enclosing contract and type below. | Return type of read_style; see its callable contract | Enclosing invocation or class/instance lifetime | 17 |
| test_merge_preserves_unmanaged_declarations_and_hover_blocks | StyleValues | Imported dependency for StyleValues in test_merge_preserves_unmanaged_declarations_and_hover_blocks; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 27 |
| test_merge_preserves_unmanaged_declarations_and_hover_blocks | merge_style | Imported dependency for merge style in test_merge_preserves_unmanaged_declarations_and_hover_blocks; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 27 |
| test_merge_preserves_unmanaged_declarations_and_hover_blocks | css | Local binding for css in test_merge_preserves_unmanaged_declarations_and_hover_blocks; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 29 |
| test_merge_preserves_unmanaged_declarations_and_hover_blocks | merged | Local binding for merged in test_merge_preserves_unmanaged_declarations_and_hover_blocks; use the enclosing contract and type below. | Return type of merge_style; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| test_zero_width_never_draws_a_border | StyleValues | Imported dependency for StyleValues in test_zero_width_never_draws_a_border; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 47 |
| test_zero_width_never_draws_a_border | merge_style | Imported dependency for merge style in test_zero_width_never_draws_a_border; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 47 |
| test_zero_width_never_draws_a_border | merged | Local binding for merged in test_zero_width_never_draws_a_border; use the enclosing contract and type below. | Return type of merge_style; see its callable contract | Enclosing invocation or class/instance lifetime | 49 |
| test_merge_creates_the_base_block_when_only_hover_exists | StyleValues | Imported dependency for StyleValues in test_merge_creates_the_base_block_when_only_hover_exists; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 60 |
| test_merge_creates_the_base_block_when_only_hover_exists | merge_style | Imported dependency for merge style in test_merge_creates_the_base_block_when_only_hover_exists; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 60 |
| test_merge_creates_the_base_block_when_only_hover_exists | merged | Local binding for merged in test_merge_creates_the_base_block_when_only_hover_exists; use the enclosing contract and type below. | Return type of merge_style; see its callable contract | Enclosing invocation or class/instance lifetime | 62 |
| test_round_trip_returns_the_saved_values | StyleValues | Imported dependency for StyleValues in test_round_trip_returns_the_saved_values; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 73 |
| test_round_trip_returns_the_saved_values | merge_style | Imported dependency for merge style in test_round_trip_returns_the_saved_values; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 73 |
| test_round_trip_returns_the_saved_values | read_style | Imported dependency for read style in test_round_trip_returns_the_saved_values; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 73 |
| test_round_trip_returns_the_saved_values | default_widget_css | Imported dependency for default widget css in test_round_trip_returns_the_saved_values; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 74 |
| test_round_trip_returns_the_saved_values | wanted | Local binding for wanted in test_round_trip_returns_the_saved_values; use the enclosing contract and type below. | Return type of StyleValues; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| test_round_trip_returns_the_saved_values | merged | Local binding for merged in test_round_trip_returns_the_saved_values; use the enclosing contract and type below. | Return type of merge_style; see its callable contract | Enclosing invocation or class/instance lifetime | 77 |
| test_field_and_caption_values_round_trip | StyleValues | Imported dependency for StyleValues in test_field_and_caption_values_round_trip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 83 |
| test_field_and_caption_values_round_trip | merge_style | Imported dependency for merge style in test_field_and_caption_values_round_trip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 83 |
| test_field_and_caption_values_round_trip | read_style | Imported dependency for read style in test_field_and_caption_values_round_trip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 83 |
| test_field_and_caption_values_round_trip | default_widget_css | Imported dependency for default widget css in test_field_and_caption_values_round_trip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 84 |
| test_field_and_caption_values_round_trip | wanted | Local binding for wanted in test_field_and_caption_values_round_trip; use the enclosing contract and type below. | Return type of StyleValues; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_field_and_caption_values_round_trip | merged | Local binding for merged in test_field_and_caption_values_round_trip; use the enclosing contract and type below. | Return type of merge_style; see its callable contract | Enclosing invocation or class/instance lifetime | 87 |
| test_merge_preserves_unmanaged_field_declarations | StyleValues | Imported dependency for StyleValues in test_merge_preserves_unmanaged_field_declarations; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 96 |
| test_merge_preserves_unmanaged_field_declarations | merge_style | Imported dependency for merge style in test_merge_preserves_unmanaged_field_declarations; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 96 |
| test_merge_preserves_unmanaged_field_declarations | css | Local binding for css in test_merge_preserves_unmanaged_field_declarations; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 98 |
| test_merge_preserves_unmanaged_field_declarations | merged | Local binding for merged in test_merge_preserves_unmanaged_field_declarations; use the enclosing contract and type below. | Return type of merge_style; see its callable contract | Enclosing invocation or class/instance lifetime | 101 |
| test_repeated_saves_never_accumulate_duplicate_blocks | StyleValues | Imported dependency for StyleValues in test_repeated_saves_never_accumulate_duplicate_blocks; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 110 |
| test_repeated_saves_never_accumulate_duplicate_blocks | merge_style | Imported dependency for merge style in test_repeated_saves_never_accumulate_duplicate_blocks; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 110 |
| test_repeated_saves_never_accumulate_duplicate_blocks | default_widget_css | Imported dependency for default widget css in test_repeated_saves_never_accumulate_duplicate_blocks; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 111 |
| test_repeated_saves_never_accumulate_duplicate_blocks | values | Local binding for values in test_repeated_saves_never_accumulate_duplicate_blocks; use the enclosing contract and type below. | Return type of StyleValues; see its callable contract | Enclosing invocation or class/instance lifetime | 113 |
| test_repeated_saves_never_accumulate_duplicate_blocks | once | Local binding for once in test_repeated_saves_never_accumulate_duplicate_blocks; use the enclosing contract and type below. | Return type of merge_style; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| test_repeated_saves_never_accumulate_duplicate_blocks | twice | Local binding for twice in test_repeated_saves_never_accumulate_duplicate_blocks; use the enclosing contract and type below. | Return type of merge_style; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| test_field_and_caption_defaults_are_read_from_a_plain_file | read_style | Imported dependency for read style in test_field_and_caption_defaults_are_read_from_a_plain_file; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 124 |
| test_field_and_caption_defaults_are_read_from_a_plain_file | default_widget_css | Imported dependency for default widget css in test_field_and_caption_defaults_are_read_from_a_plain_file; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 125 |
| test_field_and_caption_defaults_are_read_from_a_plain_file | values | Local binding for values in test_field_and_caption_defaults_are_read_from_a_plain_file; use the enclosing contract and type below. | Return type of read_style; see its callable contract | Enclosing invocation or class/instance lifetime | 127 |
| test_out_of_range_values_are_rejected | values | Parameter for values in test_out_of_range_values_are_rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 145 |
| test_out_of_range_values_are_rejected | StyleValues | Imported dependency for StyleValues in test_out_of_range_values_are_rejected; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 147 |
| test_out_of_range_values_are_rejected | merge_style | Imported dependency for merge style in test_out_of_range_values_are_rejected; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 147 |
| test_out_of_range_values_are_rejected | default_widget_css | Imported dependency for default widget css in test_out_of_range_values_are_rejected; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 148 |
| _Applications.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 157 |
| _Applications.__init__ | package | Parameter for package in _Applications.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 157 |
| _Applications.__init__ | identity | Explicit owner identity used by a session factory or fixture. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 157 |
| _Applications.__init__ | self.candidate | Attribute for candidate in _Applications.__init__; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 158 |
| _Applications.__init__ | self.saved | Attribute for saved in _Applications.__init__; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 159 |
| _Applications.owned_candidate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 161 |
| _Applications.owned_candidate | token | Parameter for token in _Applications.owned_candidate; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 161 |
| _Applications.owned_candidate | request | Parameter for request in _Applications.owned_candidate; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 161 |
| _Applications.save_file | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 165 |
| _Applications.save_file | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 165 |
| _Applications.save_file | text | Parameter for text in _Applications.save_file; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 165 |
| _Applications.save_file | identity | Explicit owner identity used by a session factory or fixture. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 165 |
| _Applications.save_file | token | Parameter for token in _Applications.save_file; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 165 |
| _Applications.save_file | request | Parameter for request in _Applications.save_file; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 165 |
| _Applications.save_file | self.saved | Attribute for saved in _Applications.save_file; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 167 |
| test_backend_load_returns_the_window_values | tmp_path | Parameter for tmp path in test_backend_load_returns_the_window_values; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 171 |
| test_backend_load_returns_the_window_values | WidgetStyleBackend | Imported dependency for WidgetStyleBackend in test_backend_load_returns_the_window_values; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 173 |
| test_backend_load_returns_the_window_values | default_widget_css | Imported dependency for default widget css in test_backend_load_returns_the_window_values; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 174 |
| test_backend_load_returns_the_window_values | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of WidgetStyleBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 177 |
| test_backend_load_returns_the_window_values | row | Local binding for row in test_backend_load_returns_the_window_values; use the enclosing contract and type below. | Return type of load; see its callable contract | Enclosing invocation or class/instance lifetime | 178 |
| test_backend_save_persists_the_merged_stylesheet | tmp_path | Parameter for tmp path in test_backend_save_persists_the_merged_stylesheet; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 193 |
| test_backend_save_persists_the_merged_stylesheet | WidgetStyleBackend | Imported dependency for WidgetStyleBackend in test_backend_save_persists_the_merged_stylesheet; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 195 |
| test_backend_save_persists_the_merged_stylesheet | default_widget_css | Imported dependency for default widget css in test_backend_save_persists_the_merged_stylesheet; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 196 |
| test_backend_save_persists_the_merged_stylesheet | applications | Local binding for applications in test_backend_save_persists_the_merged_stylesheet; use the enclosing contract and type below. | Return type of _Applications; see its callable contract | Enclosing invocation or class/instance lifetime | 199 |
| test_backend_save_persists_the_merged_stylesheet | message | Local binding for message in test_backend_save_persists_the_merged_stylesheet; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 200 |
| test_backend_save_persists_the_merged_stylesheet | token | Local binding for token in test_backend_save_persists_the_merged_stylesheet; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 200 |
| test_backend_save_persists_the_merged_stylesheet | payload | Local binding for payload in test_backend_save_persists_the_merged_stylesheet; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 200 |
| test_backend_save_persists_the_merged_stylesheet | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 209 |
| test_backend_save_persists_the_merged_stylesheet | text | Local binding for text in test_backend_save_persists_the_merged_stylesheet; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 209 |
| test_backend_payload_carries_the_widget_instance_ids | tmp_path | Parameter for tmp path in test_backend_payload_carries_the_widget_instance_ids; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 214 |
| test_backend_payload_carries_the_widget_instance_ids | package | Imported dependency for package in test_backend_payload_carries_the_widget_instance_ids; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 216 |
| test_backend_payload_carries_the_widget_instance_ids | WidgetStyleBackend | Imported dependency for WidgetStyleBackend in test_backend_payload_carries_the_widget_instance_ids; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 218 |
| test_backend_payload_carries_the_widget_instance_ids | folder | Local binding for folder in test_backend_payload_carries_the_widget_instance_ids; use the enclosing contract and type below. | Return type of package; see its callable contract | Enclosing invocation or class/instance lifetime | 220 |
| test_backend_rejects_an_unknown_widget | tmp_path | Parameter for tmp path in test_backend_rejects_an_unknown_widget; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 227 |
| test_backend_rejects_an_unknown_widget | WidgetStyleBackend | Imported dependency for WidgetStyleBackend in test_backend_rejects_an_unknown_widget; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 229 |
| test_backend_rejects_an_unknown_widget | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of WidgetStyleBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 231 |
| test_backend_rejects_an_unknown_widget | tool | Loop item for tool in test_backend_rejects_an_unknown_widget; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 232 |
| test_save_closes_the_window_on_success | WidgetStyleDialog | Imported dependency for WidgetStyleDialog in test_save_closes_the_window_on_success; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 239 |
| test_save_closes_the_window_on_success | dialog | Local binding for dialog in test_save_closes_the_window_on_success; use the enclosing contract and type below. | Return type of __new__; see its callable contract | Enclosing invocation or class/instance lifetime | 241 |
| test_save_closes_the_window_on_success | dialog._gr | Attribute for dialog. gr in test_save_closes_the_window_on_success; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 242 |
| test_save_closes_the_window_on_success | dialog.backend | Attribute for dialog.backend in test_save_closes_the_window_on_success; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 243 |
| test_save_closes_the_window_on_success | container | Local binding for container in test_save_closes_the_window_on_success; use the enclosing contract and type below. | Return type of _saved; see its callable contract | Enclosing invocation or class/instance lifetime | 246 |
| test_save_closes_the_window_on_success | message | Local binding for message in test_save_closes_the_window_on_success; use the enclosing contract and type below. | Return type of _saved; see its callable contract | Enclosing invocation or class/instance lifetime | 246 |
| test_save_closes_the_window_on_success | token | Local binding for token in test_save_closes_the_window_on_success; use the enclosing contract and type below. | Return type of _saved; see its callable contract | Enclosing invocation or class/instance lifetime | 246 |
| test_save_closes_the_window_on_success | payload | Local binding for payload in test_save_closes_the_window_on_success; use the enclosing contract and type below. | Return type of _saved; see its callable contract | Enclosing invocation or class/instance lifetime | 246 |
| test_save_keeps_the_window_open_when_a_value_is_rejected | WidgetStyleDialog | Imported dependency for WidgetStyleDialog in test_save_keeps_the_window_open_when_a_value_is_rejected; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 256 |
| test_save_keeps_the_window_open_when_a_value_is_rejected.reject | args | Parameter for args in test_save_keeps_the_window_open_when_a_value_is_rejected.reject; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 258 |
| test_save_keeps_the_window_open_when_a_value_is_rejected | dialog | Local binding for dialog in test_save_keeps_the_window_open_when_a_value_is_rejected; use the enclosing contract and type below. | Return type of __new__; see its callable contract | Enclosing invocation or class/instance lifetime | 262 |
| test_save_keeps_the_window_open_when_a_value_is_rejected | dialog._gr | Attribute for dialog. gr in test_save_keeps_the_window_open_when_a_value_is_rejected; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 263 |
| test_save_keeps_the_window_open_when_a_value_is_rejected | dialog.backend | Attribute for dialog.backend in test_save_keeps_the_window_open_when_a_value_is_rejected; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 264 |
