# tiered_energy_bill Tool Specifications

## Overview
The `tiered_energy_bill` tool calculates progressive electricity tariffs based on consumption in kWh. The tariff structure is as follows:
- First 100 kWh: 12 cents per kWh
- Next 100 kWh (101-200): 18 cents per kWh
- Remaining consumption (201+): 25 cents per kWh

## Function Signature
```python
def tiered_energy_bill(kwh: int) -> int
```

## Parameters
- `kwh` (int): Non-negative integer representing electricity consumption in kWh.
  - Must be a non-negative integer.
  - Boolean values, floats, strings, None, and negative integers are not allowed.

## Return Value
- Returns an integer representing the total cost in cents.
- The result is exact with no rounding.

## Validation Rules
- Raises `ValueError` for:
  - Negative integers
  - Floats (including 1.0)
  - Strings
  - None
  - Boolean values

## Examples
```python
tiered_energy_bill(50)   # Returns: 600 (50 * 12)
tiered_energy_bill(150)  # Returns: 1950 (100*12 + 50*18)
tiered_energy_bill(250)  # Returns: 3750 (100*12 + 100*18 + 50*25)
```

## Arithmetic Details
- Tier 1 (0-100 kWh): 12 cents/kWh
- Tier 2 (101-200 kWh): 18 cents/kWh
- Tier 3 (201+ kWh): 25 cents/kWh

## Implementation Notes
This is a pure standalone function with no side effects.