"""
Random Number Generator Tool

This tool generates a single random integer between two given numbers (inclusive).
It is designed as a pure standalone function with strict input validation and security considerations.
"""

import random
from typing import Annotated

def random_number_generator(
    min_value: Annotated[int, "Minimum value (inclusive)"], 
    max_value: Annotated[int, "Maximum value (inclusive)"]
) -> Annotated[int, "Random integer between min_value and max_value (inclusive)"]:
    """
    Generate a single random integer between min_value and max_value (inclusive).
    
    Args:
        min_value: The minimum value (inclusive) for the random number generation
        max_value: The maximum value (inclusive) for the random number generation
        
    Returns:
        Random integer between min_value and max_value (inclusive)
        
    Raises:
        TypeError: If either parameter is not an integer
        ValueError: If min_value is greater than max_value
    """
    # Validate input types
    if not isinstance(min_value, int):
        raise TypeError("min_value must be an integer")
        
    if not isinstance(max_value, int):
        raise TypeError("max_value must be an integer")
        
    # Validate range
    if min_value > max_value:
        raise ValueError("min_value must be less than or equal to max_value")
        
    # Generate and return random number
    return random.randint(min_value, max_value)