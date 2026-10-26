# tiered_energy_bill Tool Specifications

## Overview
The `tiered_energy_bill` tool calculates electricity bills based on a tiered pricing structure. It accepts a consumption value in kWh and returns the total cost in cents as an integer.

## Function Signature
```python
def tiered_energy_bill(kwh: int) -> int
```

## Parameters
- `kwh` (int): The amount of electricity consumed in kilowatt-hours (kWh). Must be a non-negative integer.

## Return Type
- `int`: Total cost of the electricity consumption in cents. The result is exact and does not include any rounding.

## Pricing Tiers
1. **First 100 kWh**: 12 cents/kWh
2. **Next 100 kWh (101-200)**: 18 cents/kWh
3. **Remaining kWh (201+)**: 25 cents/kWh

## Validation Rules
The function strictly validates the input:
- Only non-negative integers are accepted.
- Any other type including `bool`, `float` (even if whole number like `1.0`), `str`, `None`, or negative integers will raise a `ValueError`.

## Examples
```python
tiered_energy_bill(50)   # Returns 600 (50 * 12)
tiered_energy_bill(150)  # Returns 2100 (100*12 + 50*18)
tiered_energy_bill(250)  # Returns 4250 (100*12 + 100*18 + 50*25)
```

## Error Handling
- `ValueError` is raised for invalid inputs such as:
  - Negative integers
  - Floats (even whole numbers)
  - Strings
  - Booleans
  - None

## Implementation Notes
This function is designed to be a pure, standalone top-level function with no external dependencies. It performs exact arithmetic without rounding and strictly enforces input validation.