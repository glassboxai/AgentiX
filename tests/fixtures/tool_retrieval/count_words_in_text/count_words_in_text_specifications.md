# count_words_in_text Specifications

## Overview
The `count_words_in_text` tool takes a text input and returns the number of words present in that text. A word is defined as a sequence of characters separated by whitespace.

## Function Signature
```python
def count_words_in_text(text: typing.Annotated[str, "The input text to count words in"]) -> typing.Annotated[int, "The number of words in the input text"]:
    ...
```

## Parameters
- `text` (str): The input text to analyze. Must be a non-empty string.

## Returns
- int: The number of words in the input text.

## Constraints
- Input must be a string.
- Empty strings return 0.
- Words are separated by one or more whitespace characters (spaces, tabs, newlines).
- Punctuation attached to words is considered part of the word.

## Edge Cases
- Empty string: Returns 0.
- String with only whitespace: Returns 0.
- Single word: Returns 1.
- Multiple spaces between words: Counted as one separator.