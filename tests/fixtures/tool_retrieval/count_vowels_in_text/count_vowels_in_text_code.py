"""
Count vowels in text.

This module provides a function to count the number of vowels in a given text.
Vowels are defined as 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase).
Non-alphabetic characters do not count as vowels.
"""

from typing import Annotated


def count_vowels_in_text(text: Annotated[str, "The input text to analyze for vowels."]) -> Annotated[int, "The total number of vowels in the input text."]:
    """
    Count the number of vowels in the given text.
    
    Vowels are defined as 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase).
    Non-alphabetic characters do not count as vowels.
    
    Args:
        text: The input text to analyze for vowels. Must be a string.
        
    Returns:
        The total number of vowels in the input text.
        
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
            
    return count