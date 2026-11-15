# count_vowels_in_text Specifications

## Overview
The `count_vowels_in_text` function takes a text input and returns the number of vowels present in that text. Vowels are defined as the letters 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase).

## Function Signature
```python
def count_vowels_in_text(text: str) -> int:
    ...
```

## Parameters
- `text` (`str`): The input text to analyze for vowels. Must be a string.

## Returns
- `int`: The total number of vowels in the input text.

## Constraints
- The function must handle all ASCII characters.
- Case-insensitive: both uppercase and lowercase vowels are counted.
- Non-alphabetic characters (e.g., digits, punctuation) do not count as vowels.
- Empty strings return 0.

## Edge Cases
- Input is an empty string (`""`) → Returns `0`
- Input contains no vowels → Returns `0`
- Input contains only vowels → Returns length of input
- Input contains mixed case vowels → Counts all vowels regardless of case

## Validation
- If the input is not a string, a `TypeError` is raised.