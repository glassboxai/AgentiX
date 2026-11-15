"""
Basic Calculator

A standalone Python function that performs basic arithmetic operations between two numbers.
"""

from typing import Annotated

def basic_calculator(
    num1: Annotated[float, "First number for the operation"],
    operator: Annotated[str, "Arithmetic operator (+, -, *, /)"],
    num2: Annotated[float, "Second number for the operation"]
) -> Annotated[float, "Result of the arithmetic operation"]:
    """
    Perform basic arithmetic operations between two numbers.
    
    Args:
        num1: First number for the operation
        operator: Arithmetic operator to use (+, -, *, /)
        num2: Second number for the operation
        
    Returns:
        Result of the arithmetic operation
        
    Raises:
        ValueError: For invalid operators or division by zero
        TypeError: For non-numeric inputs
    """
    # Validate numeric inputs
    if not isinstance(num1, (int, float)):
        raise TypeError("First operand must be a number")
        
    if not isinstance(num2, (int, float)):
        raise TypeError("Second operand must be a number")
        
    # Validate operator
    valid_operators = ['+', '-', '*', '/']
    if operator not in valid_operators:
        raise ValueError(f"Invalid operator '{operator}'. Must be one of {valid_operators}")
        
    # Perform calculation
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        return num1 / num2