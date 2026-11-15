# Basic Calculator Specifications

## Overview
A standalone Python function that performs basic arithmetic operations between two numbers.

## Function Signature
```python
def basic_calculator(
    num1: Annotated[float, "First number for the operation"],
    operator: Annotated[str, "Arithmetic operator (+, -, *, /)"],
    num2: Annotated[float, "Second number for the operation"]
) -> Annotated[float, "Result of the arithmetic operation"]:
```

## Parameters
- `num1` (float): The first operand in the calculation
- `operator` (str): The arithmetic operator to use (+, -, *, /)
- `num2` (float): The second operand in the calculation

## Return Value
- float: The result of applying the operator to num1 and num2

## Valid Operations
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

## Constraints
- All parameters must be provided
- `num1` and `num2` must be numeric types (int or float)
- `operator` must be one of: '+', '-', '*', '/'
- Division by zero must raise a ValueError
- Invalid operators must raise a ValueError

## Error Handling
- Raises ValueError for invalid operators
- Raises ValueError for division by zero
- Raises TypeError for non-numeric inputs