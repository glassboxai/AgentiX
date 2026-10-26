# tiered_energy_bill Tool Specifications

## Overview
The `tiered_energy_bill` tool calculates electricity bills based on a tiered pricing structure. It accepts consumption in kilowatt-hours (kWh) and returns the total cost in cents.

## Function Signature
```python
def tiered_energy_bill(kwh: int) -> int
```

## Parameters
- `kwh` (int): The amount of electricity consumed in kilowatt-hours.
  - Must be a non-negative integer.
  - Any input that is not an integer or is negative will raise a `ValueError`.

## Return Value
- Returns the total cost of electricity consumption in cents as an integer.
- No rounding is performed; exact arithmetic is maintained.

## Pricing Tiers
1. **First 100 kWh**: 12 cents/kWh
2. **Next 100 kWh (101-200)**: 18 cents/kWh
3. **Remaining kWh (201+)**: 25 cents/kWh

## Validation Rules
- Input must be an integer.
- Input must be non-negative.
- Any input that is:
  - A boolean (`True`, `False`)
  - A float (including `1.0`)
  - A string
  - `None`
  - Negative
will raise a `ValueError`.

## Example Calculation for 250 kWh
- First 100 kWh: 100 × 12 = 1200 cents
- Next 100 kWh: 100 × 18 = 1800 cents
- Remaining 50 kWh: 50 × 25 = 1250 cents
- Total: 1200 + 1800 + 1250 = 4250 cents

## Implementation Notes
- The function is pure and stateless.
- All arithmetic is performed using integer operations to ensure exactness.