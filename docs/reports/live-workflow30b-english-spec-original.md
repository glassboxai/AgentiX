# tiered_energy_bill Tool Specifications

## Overview
The `tiered_energy_bill` tool calculates progressive electricity tariffs based on consumption in kWh. The tariff structure is as follows:
- First 100 kWh: 12 cents per kWh
- Next 100 kWh (101-200): 18 cents per kWh
- All remaining consumption (201+): 25 cents per kWh

## Function Signature
```python
def tiered_energy_bill(kwh: int) -> int
```

## Parameters
- `kwh` (int): Non-negative integer representing electricity consumption in kilowatt-hours.
  - Must be a non-negative integer.
  - Boolean values, floats (including 1.0), strings, None, and negative integers are invalid.

## Return Value
- Returns an integer representing the total cost in cents.
- The result is exact with no rounding.

## Validation Rules
- Raises `ValueError` for any input that is not a non-negative integer:
  - Negative integers
  - Floats (including 1.0)
  - Strings
  - Boolean values
  - None

## Example Calculation
For 250 kWh:
- First 100 kWh: 100 × 12 = 1200 cents
- Next 100 kWh: 100 × 18 = 1800 cents
- Remaining 50 kWh: 50 × 25 = 1250 cents
- Total: 1200 + 1800 + 1250 = 4250 cents

## Implementation Notes
This function is a pure standalone top-level function.