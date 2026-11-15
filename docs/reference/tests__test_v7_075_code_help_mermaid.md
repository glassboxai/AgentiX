# Reference for tests/test_v7_075_code_help_mermaid.py

V7-075: code help renders fenced Mermaid diagrams from a local, pinned bundle.

Source fingerprint: e8238209fd96c5fc148184f6fd46991b05ee5e1ba03c969889dac714e8a2afab

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_transcript_component_type_is_markdown

Catch a regression back to a Textbox, which cannot render a diagram.

Kind: callable. Declared return: Not declared / class. Source line: 15.

### test_transcript_component_type_is_markdown.Backend

Minimal composition boundary; the helper only stores it.

Kind: class. Declared return: Not declared / class. Source line: 21.

### test_launch_options_embed_the_local_bundle_without_a_network_url

Catch a CDN reference or a renderer that never reaches the page.

Kind: callable. Declared return: Not declared / class. Source line: 42.

### test_vendored_bundle_matches_the_pinned_digest

Catch an unreviewed replacement of the third-party bundle.

Kind: callable. Declared return: Not declared / class. Source line: 55.

### test_renderer_only_targets_the_code_help_transcript

Catch a global selector that would render untrusted application output.

Kind: callable. Declared return: Not declared / class. Source line: 61.

### test_real_gradio_launch_publishes_mermaid_and_renders_a_fence

Catch the eval-scope defect where the bundle's global assignment throws.

Kind: callable. Declared return: Not declared / class. Source line: 70.

### test_fenced_mermaid_renders_as_svg_inside_the_helper

Render a real diagram, keep other code blocks inert and re-render on update.

Kind: callable. Declared return: Not declared / class. Source line: 114.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | ASSETS | Module binding for ASSETS in module; use the enclosing contract and type below. | Return type of Path; see its callable contract | Module/process lifetime | 8 |
| module | MERMAID_BUNDLE | Module binding for MERMAID BUNDLE in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 9 |
| module | MERMAID_RENDERER | Module binding for MERMAID RENDERER in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 10 |
| module | MERMAID_DIGEST | Module binding for MERMAID DIGEST in module; use the enclosing contract and type below. | str | Module/process lifetime | 11 |
| test_transcript_component_type_is_markdown | gr | Imported dependency for gr in test_transcript_component_type_is_markdown; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 17 |
| test_transcript_component_type_is_markdown | build_chathelper | Imported dependency for build chathelper in test_transcript_component_type_is_markdown; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 19 |
| test_transcript_component_type_is_markdown.Backend | sessions | Local binding for sessions in test_transcript_component_type_is_markdown.Backend; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 24 |
| test_transcript_component_type_is_markdown | blocks | Managed resource for blocks in test_transcript_component_type_is_markdown; use the enclosing contract and type below. | Return type of Blocks; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 26 |
| test_transcript_component_type_is_markdown.lambda_30 | callback | Callback parameter for callback in test_transcript_component_type_is_markdown.lambda_30; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 30 |
| test_transcript_component_type_is_markdown | components | Local binding for components in test_transcript_component_type_is_markdown; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 35 |
| test_transcript_component_type_is_markdown.comprehension_35 | component | Comprehension item for component in test_transcript_component_type_is_markdown.comprehension_35; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 37 |
| test_launch_options_embed_the_local_bundle_without_a_network_url | launch_options | Imported dependency for launch options in test_launch_options_embed_the_local_bundle_without_a_network_url; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 44 |
| test_launch_options_embed_the_local_bundle_without_a_network_url | script | Local binding for script in test_launch_options_embed_the_local_bundle_without_a_network_url; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 46 |
| test_launch_options_embed_the_local_bundle_without_a_network_url | host | Loop item for host in test_launch_options_embed_the_local_bundle_without_a_network_url; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 50 |
| test_renderer_only_targets_the_code_help_transcript | source | Explicit source document or source-code text; never imported for reference generation. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| test_real_gradio_launch_publishes_mermaid_and_renders_a_fence | tmp_path | Parameter for tmp path in test_real_gradio_launch_publishes_mermaid_and_renders_a_fence; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 70 |
| test_real_gradio_launch_publishes_mermaid_and_renders_a_fence | os | Imported dependency for os in test_real_gradio_launch_publishes_mermaid_and_renders_a_fence; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 72 |
| test_real_gradio_launch_publishes_mermaid_and_renders_a_fence | gr | Imported dependency for gr in test_real_gradio_launch_publishes_mermaid_and_renders_a_fence; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 74 |
| test_real_gradio_launch_publishes_mermaid_and_renders_a_fence | expect | Imported dependency for expect in test_real_gradio_launch_publishes_mermaid_and_renders_a_fence; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 75 |
| test_real_gradio_launch_publishes_mermaid_and_renders_a_fence | sync_playwright | Imported dependency for sync playwright in test_real_gradio_launch_publishes_mermaid_and_renders_a_fence; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 75 |
| test_real_gradio_launch_publishes_mermaid_and_renders_a_fence | free_port | Imported dependency for free port in test_real_gradio_launch_publishes_mermaid_and_renders_a_fence; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 76 |
| test_real_gradio_launch_publishes_mermaid_and_renders_a_fence | launch_options | Imported dependency for launch options in test_real_gradio_launch_publishes_mermaid_and_renders_a_fence; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 78 |
| test_real_gradio_launch_publishes_mermaid_and_renders_a_fence | port | Local binding for port in test_real_gradio_launch_publishes_mermaid_and_renders_a_fence; use the enclosing contract and type below. | Return type of free_port; see its callable contract | Enclosing invocation or class/instance lifetime | 80 |
| test_real_gradio_launch_publishes_mermaid_and_renders_a_fence | demo | Managed resource for demo in test_real_gradio_launch_publishes_mermaid_and_renders_a_fence; use the enclosing contract and type below. | Return type of Blocks; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 81 |
| test_real_gradio_launch_publishes_mermaid_and_renders_a_fence | driver | Managed resource for driver in test_real_gradio_launch_publishes_mermaid_and_renders_a_fence; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 94 |
| test_real_gradio_launch_publishes_mermaid_and_renders_a_fence | browser | Local binding for browser in test_real_gradio_launch_publishes_mermaid_and_renders_a_fence; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 95 |
| test_real_gradio_launch_publishes_mermaid_and_renders_a_fence | page | Local binding for page in test_real_gradio_launch_publishes_mermaid_and_renders_a_fence; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 99 |
| test_real_gradio_launch_publishes_mermaid_and_renders_a_fence | errors | Local binding for errors in test_real_gradio_launch_publishes_mermaid_and_renders_a_fence; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 100 |
| test_real_gradio_launch_publishes_mermaid_and_renders_a_fence.lambda_101 | error | Callback parameter for error in test_real_gradio_launch_publishes_mermaid_and_renders_a_fence.lambda_101; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 101 |
| test_fenced_mermaid_renders_as_svg_inside_the_helper | tmp_path | Parameter for tmp path in test_fenced_mermaid_renders_as_svg_inside_the_helper; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 114 |
| test_fenced_mermaid_renders_as_svg_inside_the_helper | os | Imported dependency for os in test_fenced_mermaid_renders_as_svg_inside_the_helper; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 116 |
| test_fenced_mermaid_renders_as_svg_inside_the_helper | expect | Imported dependency for expect in test_fenced_mermaid_renders_as_svg_inside_the_helper; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 118 |
| test_fenced_mermaid_renders_as_svg_inside_the_helper | sync_playwright | Imported dependency for sync playwright in test_fenced_mermaid_renders_as_svg_inside_the_helper; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 118 |
| test_fenced_mermaid_renders_as_svg_inside_the_helper | html | Local binding for html in test_fenced_mermaid_renders_as_svg_inside_the_helper; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 120 |
| test_fenced_mermaid_renders_as_svg_inside_the_helper | driver | Managed resource for driver in test_fenced_mermaid_renders_as_svg_inside_the_helper; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 126 |
| test_fenced_mermaid_renders_as_svg_inside_the_helper | browser | Local binding for browser in test_fenced_mermaid_renders_as_svg_inside_the_helper; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 127 |
| test_fenced_mermaid_renders_as_svg_inside_the_helper | page | Local binding for page in test_fenced_mermaid_renders_as_svg_inside_the_helper; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 131 |
