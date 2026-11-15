# Random Number Generator Tool Specifications

## Overview
This tool generates a single random integer between two given numbers (inclusive). It is designed as a pure standalone function with strict input validation and security considerations.

## Function Signature
```python
def random_number_generator(
    min_value: Annotated[int, "Minimum value (inclusive)"], 
    max_value: Annotated[int, "Maximum value (inclusive)"]
) -> Annotated[int, "Random integer between min_value and max_value (inclusive)"]:
```

## Parameters
- `min_value` (int): The minimum value (inclusive) for the random number generation
- `max_value` (int): The maximum value (inclusive) for the random number generation

## Return Value
- Returns a single random integer between min_value and max_value (inclusive)

## Constraints and Validations
1. Both parameters must be integers
2. min_value must be less than or equal to max_value
3. The function generates exactly one random number within the specified range
4. No external dependencies or file I/O operations

## Edge Cases Handled
- When min_value equals max_value, returns that value
- Negative numbers are supported
- Zero is supported as a valid input
- Large integers are supported (within Python's integer limits)

## Security Considerations
- No PII or confidential data handling
- No file system access
- No external network calls
- Input validation prevents invalid ranges