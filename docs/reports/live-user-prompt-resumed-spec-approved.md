# Electricity Bill Calculator - Specifications

## Overview
This tool calculates the electricity bill for a household based on tiered pricing:
- First 100 kWh: €0.12 per kWh
- Next 100 kWh (101-200): €0.18 per kWh
- Additional consumption (201+): €0.25 per kWh

## Function Specification

### `calculate_electricity_bill(consumption_kwh: float) -> dict`
Calculates the electricity bill based on tiered pricing.

#### Parameters
- **consumption_kwh** (float): Total electricity consumption in kilowatt-hours (kWh)
  - Must be non-negative
  - Must be a finite int or float; boolean values are not consumption and raise TypeError

#### Returns
- **dict**: A dictionary containing:
  - `total_cost` (float): Total bill amount in euros
  - `breakdown` (list): List of dictionaries describing each tier's usage and cost
    - Each item has keys: `tier`, `range`, `kwh`, `rate`, `cost`

#### Invalid Input Handling
- Raises **TypeError** if input is not a number
- Raises **ValueError** if input is negative, infinite or NaN

## Example Usage
```python
result = calculate_electricity_bill(350)
print(result['total_cost'])  # Output: 67.50
```

## Tier Breakdown for 350 kWh
1. First 100 kWh: €0.12/kWh → €12.00
2. Next 100 kWh: €0.18/kWh → €18.00
3. Remaining 150 kWh: €0.25/kWh → €37.50
Total: €67.50

## Test Cases
- Normal case: 350 kWh → €67.50
- Boundary case: 100 kWh → €12.00
- Boundary case: 200 kWh → €30.00
- Edge case: 0 kWh → €0.00
- Invalid input: negative value → ValueError
- Invalid input: non-numeric → TypeError
## Output consistency
- Return all three tier entries in order, including zero usage.
- Monetary amounts are expressed in euros and rounded to two decimal places.
- Tier usage must sum to the requested consumption.
