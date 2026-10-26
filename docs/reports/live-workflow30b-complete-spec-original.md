# tiered_energy_bill Tool Specifications

## Overview
The `tiered_energy_bill` tool calculates electricity bills based on a tiered pricing structure. It takes the total energy consumption in kilowatt-hours (kWh) and returns the total cost in cents.

## Function Signature
```python
def tiered_energy_bill(kwh: int) -> int
```

## Parameters
- `kwh` (int): The total electricity consumption in kilowatt-hours. Must be a non-negative integer.
  - Invalid types: bool, float (including 1.0), str, None, and negative integers.
  - Valid range: [0, ∞)

## Return Value
- Returns an integer representing the total cost in cents.
- The calculation follows these tiers:
  1. First 100 kWh: 12 cents/kWh
  2. Next 100 kWh (101-200): 18 cents/kWh
  3. Remaining kWh (201+): 25 cents/kWh

## Behavior
- For `kwh` values:
  - If `kwh` is a non-negative integer, the function computes the cost using the tiered pricing.
  - If `kwh` is any other type (bool, float, str, None, or negative int), a `ValueError` is raised.

## Examples
```python
tiered_energy_bill(50)   # Returns: 600 (50 * 12)
tiered_energy_bill(150)  # Returns: 2100 (100*12 + 50*18)
tiered_energy_bill(250)  # Returns: 3750 (100*12 + 100*18 + 50*25)
```

## Validation
- Input validation strictly enforces integer types.
- Negative integers, floats, strings, booleans, and None are not allowed.
- All inputs must be non-negative integers.

## Notes
- The function is pure and does not have side effects.
- No rounding occurs; all calculations are exact.