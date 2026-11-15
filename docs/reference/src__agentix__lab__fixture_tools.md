# Reference for src/agentix/lab/fixture_tools.py

Trusted standard-library-only example tools staged as bytes into AppContainer.

These authored examples are maintained application fixtures, not generated artifacts.
The host validates all inputs/outputs; these annotations also document each contract.

Source fingerprint: 64f0d140769c90995e2fb44527a392734cf37185a6f7ab7b95fe76453decc562

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### normalize_text

Collapse whitespace and strip leading/trailing whitespace; preserve letters.

Kind: callable. Declared return: Annotated[str, 'Whitespace-normalized text']. Source line: 10.

### count_words

Count nonempty whitespace-separated words; empty input returns zero.

Kind: callable. Declared return: Annotated[int, 'Nonnegative whitespace-delimited word count']. Source line: 17.

### count_vowels

Count ASCII vowels case-insensitively without accent normalization.

Kind: callable. Declared return: Annotated[int, 'Nonnegative ASCII vowel count']. Source line: 24.

### summarize

Combine counts without inventing an uncomputed vowel result.

Kind: callable. Declared return: Annotated[dict, 'Structured counts; absent vowels remain null']. Source line: 31.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Annotated | Imported dependency for Annotated in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| normalize_text | text | Parameter for text in normalize_text; use the enclosing contract and type below. | Annotated[str, 'Text up to 16000 characters'] | Enclosing invocation or class/instance lifetime | 11 |
| count_words | text | Parameter for text in count_words; use the enclosing contract and type below. | Annotated[str, 'Text up to 16000 characters'] | Enclosing invocation or class/instance lifetime | 18 |
| count_vowels | text | Parameter for text in count_vowels; use the enclosing contract and type below. | Annotated[str, 'Text up to 16000 characters'] | Enclosing invocation or class/instance lifetime | 25 |
| count_vowels.comprehension_28 | character | Comprehension item for character in count_vowels.comprehension_28; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 28 |
| summarize | words | Parameter for words in summarize; use the enclosing contract and type below. | Annotated[int, 'Nonnegative word count'] | Enclosing invocation or class/instance lifetime | 32 |
| summarize | vowels | Parameter for vowels in summarize; use the enclosing contract and type below. | Annotated[int &#124; None, 'Optional nonnegative vowel count'] | Enclosing invocation or class/instance lifetime | 33 |
