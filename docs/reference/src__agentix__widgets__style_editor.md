# Reference for src/agentix/widgets/style_editor.py

Read and rewrite the six owner-editable declarations of one widget stylesheet.

The window edits a closed set of declarations inside the single scoped block that
``agentix.widgets.styles`` already accepts. Every other declaration and every
``:hover`` block is preserved byte-for-byte in meaning, and the merged result is
validated again before it can reach disk.

Source fingerprint: c277dcda8e402e6121d577f13e5b48e1747cc55eff30faf4a94fb1600ed2c704

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### StyleValues

The nine values the window owns, already normalised to their stored form.

Kind: class. Declared return: Not declared / class. Source line: 59.

### _pixels

Read one bounded pixel length, falling back to the palette default.

Kind: callable. Declared return: int. Source line: 73.

### _color

Accept only a full hexadecimal colour so the grammar stays satisfied.

Kind: callable. Declared return: str. Source line: 79.

### read_style

Return the managed values of the base, field and caption blocks.

A missing declaration, an unparsable length or an unsupported family yields the
documented default instead of an error: the window must open on any valid file.

Kind: callable. Declared return: StyleValues. Source line: 84.

### checked

Reject out-of-range input before it can reach the stylesheet grammar.

Kind: callable. Declared return: StyleValues. Source line: 125.

### merge_style

Rewrite only the managed declarations, preserving every other block.

The base block keeps its unmanaged declarations in their original order and the
managed ones are appended in a fixed order. ``border-style`` is derived so a
non-zero width is always visible and a zero width never draws a border. The field
and caption blocks are rewritten the same way, so a padding or a colour that the
window does not own survives.

Kind: callable. Declared return: str. Source line: 158.

### merge_style.first

Return the first non-hover block of this role for the given suffixes.

Kind: callable. Declared return: re.Match | None. Source line: 186.

### merge_style.rewrite

Keep unmanaged declarations of one block, then append the owned ones.

Kind: callable. Declared return: str. Source line: 199.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | validate_widget_css | Imported dependency for validate widget css in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | FONTS | Module binding for FONTS in module; use the enclosing contract and type below. | tuple | Module/process lifetime | 14 |
| module | MANAGED | Module binding for MANAGED in module; use the enclosing contract and type below. | tuple | Module/process lifetime | 25 |
| module | FIELD_MANAGED | Module binding for FIELD MANAGED in module; use the enclosing contract and type below. | tuple | Module/process lifetime | 37 |
| module | LABEL_MANAGED | Module binding for LABEL MANAGED in module; use the enclosing contract and type below. | tuple | Module/process lifetime | 38 |
| module | DEFAULT_BORDER | Module binding for DEFAULT BORDER in module; use the enclosing contract and type below. | str | Module/process lifetime | 40 |
| module | DEFAULT_BACKGROUND | Module binding for DEFAULT BACKGROUND in module; use the enclosing contract and type below. | str | Module/process lifetime | 41 |
| module | DEFAULT_SIZE | Module binding for DEFAULT SIZE in module; use the enclosing contract and type below. | int | Module/process lifetime | 42 |
| module | MAX_RADIUS | Module binding for MAX RADIUS in module; use the enclosing contract and type below. | int | Module/process lifetime | 43 |
| module | MAX_WIDTH | Module binding for MAX WIDTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 44 |
| module | HEX | Module binding for HEX in module; use the enclosing contract and type below. | Return type of compile; see its callable contract | Module/process lifetime | 46 |
| module | PIXELS | Module binding for PIXELS in module; use the enclosing contract and type below. | Return type of compile; see its callable contract | Module/process lifetime | 47 |
| module | BLOCK | Module binding for BLOCK in module; use the enclosing contract and type below. | Return type of compile; see its callable contract | Module/process lifetime | 48 |
| module | FIELD_SUFFIXES | Module binding for FIELD SUFFIXES in module; use the enclosing contract and type below. | tuple | Module/process lifetime | 54 |
| module | LABEL_SUFFIXES | Module binding for LABEL SUFFIXES in module; use the enclosing contract and type below. | tuple | Module/process lifetime | 55 |
| StyleValues | radius | Typed binding for radius in StyleValues; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 62 |
| StyleValues | width | Typed binding for width in StyleValues; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 63 |
| StyleValues | border_color | Typed binding for border color in StyleValues; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 64 |
| StyleValues | background | Typed binding for background in StyleValues; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 65 |
| StyleValues | font_family | Typed binding for font family in StyleValues; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 66 |
| StyleValues | font_size | Typed binding for font size in StyleValues; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 67 |
| StyleValues | field_background | Typed binding for field background in StyleValues; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 68 |
| StyleValues | label_font_family | Typed binding for label font family in StyleValues; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 69 |
| StyleValues | label_font_size | Typed binding for label font size in StyleValues; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 70 |
| _pixels | value | Value at the current validation/rendering boundary; apply the enclosing contract. | str | Enclosing invocation or class/instance lifetime | 73 |
| _pixels | default | Parameter for default in _pixels; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 73 |
| _pixels | match | Local binding for match in _pixels; use the enclosing contract and type below. | Return type of fullmatch; see its callable contract | Enclosing invocation or class/instance lifetime | 75 |
| _color | value | Value at the current validation/rendering boundary; apply the enclosing contract. | str | Enclosing invocation or class/instance lifetime | 79 |
| _color | default | Parameter for default in _color; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 79 |
| read_style | css | Parameter for css in read_style; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 84 |
| read_style | role | Parameter for role in read_style; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 84 |
| read_style | declarations | Typed binding for declarations in read_style; use the enclosing contract and type below. | dict[str, str] | Enclosing invocation or class/instance lifetime | 90 |
| read_style | field | Typed binding for field in read_style; use the enclosing contract and type below. | dict[str, str] | Enclosing invocation or class/instance lifetime | 91 |
| read_style | label | Typed binding for label in read_style; use the enclosing contract and type below. | dict[str, str] | Enclosing invocation or class/instance lifetime | 92 |
| read_style | match | Loop item for match in read_style; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 93 |
| read_style | suffix | Local binding for suffix in read_style; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 96 |
| read_style | target | Local binding for target in read_style; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 97, 99, 101 |
| read_style | declaration | Loop item for declaration in read_style; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 102 |
| read_style | name | Current identifier selected by parsing, lookup or dependency registration. | Return type of partition; see its callable contract | Enclosing invocation or class/instance lifetime | 103 |
| read_style | separator | Local binding for separator in read_style; use the enclosing contract and type below. | Return type of partition; see its callable contract | Enclosing invocation or class/instance lifetime | 103 |
| read_style | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of partition; see its callable contract | Enclosing invocation or class/instance lifetime | 103 |
| read_style | family | Local binding for family in read_style; use the enclosing contract and type below. | Return type of strip; see its callable contract | Enclosing invocation or class/instance lifetime | 106 |
| read_style | label_family | Local binding for label family in read_style; use the enclosing contract and type below. | Return type of strip; see its callable contract | Enclosing invocation or class/instance lifetime | 107 |
| checked | values | Parameter for values in checked; use the enclosing contract and type below. | StyleValues | Enclosing invocation or class/instance lifetime | 125 |
| merge_style | css | Parameter for css in merge_style; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 158 |
| merge_style | role | Parameter for role in merge_style; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 158 |
| merge_style | values | Parameter for values in merge_style; use the enclosing contract and type below. | StyleValues | Enclosing invocation or class/instance lifetime | 158, 168 |
| merge_style | selector | Local binding for selector in merge_style; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 169 |
| merge_style | managed | Local binding for managed in merge_style; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 170 |
| merge_style | field | Local binding for field in merge_style; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 179 |
| merge_style | label | Local binding for label in merge_style; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 180 |
| merge_style | blocks | Local binding for blocks in merge_style; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 184 |
| merge_style.first | suffixes | Parameter for suffixes in merge_style.first; use the enclosing contract and type below. | tuple[str, ...] | Enclosing invocation or class/instance lifetime | 186 |
| merge_style.first.comprehension_189 | match | Comprehension item for match in merge_style.first.comprehension_189; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 191 |
| merge_style.rewrite | match | Parameter for match in merge_style.rewrite; use the enclosing contract and type below. | re.Match &#124; None | Enclosing invocation or class/instance lifetime | 199 |
| merge_style.rewrite | owned | Parameter for owned in merge_style.rewrite; use the enclosing contract and type below. | dict[str, str] | Enclosing invocation or class/instance lifetime | 199 |
| merge_style.rewrite | kept | Typed binding for kept in merge_style.rewrite; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 201 |
| merge_style.rewrite | declaration | Loop item for declaration in merge_style.rewrite; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 203 |
| merge_style.rewrite | name | Current identifier selected by parsing, lookup or dependency registration. | Return type of partition; see its callable contract | Enclosing invocation or class/instance lifetime | 204 |
| merge_style.rewrite | separator | Local binding for separator in merge_style.rewrite; use the enclosing contract and type below. | Return type of partition; see its callable contract | Enclosing invocation or class/instance lifetime | 204 |
| merge_style.rewrite | _ | Local binding for  in merge_style.rewrite; use the enclosing contract and type below. | Return type of partition; see its callable contract | Enclosing invocation or class/instance lifetime | 204 |
| merge_style.rewrite.comprehension_207 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 207 |
| merge_style.rewrite.comprehension_207 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 207 |
| merge_style | base_match | Local binding for base match in merge_style; use the enclosing contract and type below. | Return type of first; see its callable contract | Enclosing invocation or class/instance lifetime | 209 |
| merge_style | rendered | Local binding for rendered in merge_style; use the enclosing contract and type below. | Return type of rewrite; see its callable contract | Enclosing invocation or class/instance lifetime | 210 |
| merge_style | field_input | Local binding for field input in merge_style; use the enclosing contract and type below. | Return type of first; see its callable contract | Enclosing invocation or class/instance lifetime | 211 |
| merge_style | field_textarea | Local binding for field textarea in merge_style; use the enclosing contract and type below. | Return type of first; see its callable contract | Enclosing invocation or class/instance lifetime | 212 |
| merge_style | label_match | Local binding for label match in merge_style; use the enclosing contract and type below. | Return type of first; see its callable contract | Enclosing invocation or class/instance lifetime | 213 |
| merge_style | owned_blocks | Local binding for owned blocks in merge_style; use the enclosing contract and type below. | set | Enclosing invocation or class/instance lifetime | 216 |
| merge_style.comprehension_216 | match | Comprehension item for match in merge_style.comprehension_216; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 218 |
| merge_style | tail | Local binding for tail in merge_style; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 223 |
| merge_style.comprehension_223 | match | Comprehension item for match in merge_style.comprehension_223; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 223 |
| merge_style | merged | Local binding for merged in merge_style; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 224 |
