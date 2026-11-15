"""
Tool to count the number of words in a given text.

A word is defined as a sequence of characters separated by whitespace.
"""

import typing

def count_words_in_text(text: typing.Annotated[str, "The input text to count words in"]) -> typing.Annotated[int, "The number of words in the input text"]:
    """
    Count the number of words in the provided text.
    
    A word is defined as a sequence of characters separated by whitespace.
    
    Args:
        text (str): The input text to analyze. Must be a non-empty string.
        
    Returns:
        int: The number of words in the input text.
        
    Examples:
        >>> count_words_in_text("Hello world")
        2
        >>> count_words_in_text("")
        0
        >>> count_words_in_text("   ")
        0
    """
    # Validate input
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    # Handle empty string or string with only whitespace
    if not text or not text.strip():
        return 0
    
    # Split by whitespace and filter out empty strings
    words = text.split()
    return len(words)