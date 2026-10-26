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
  - Must be a finite int or float; booleans are not consumption values and must raise TypeError

#### Returns
- **dict**: A dictionary containing:
  - `total_cost_euros` (float): Total bill amount in euros
  - `breakdown` (list of dicts): Cost breakdown by tier
    - Each dict contains:
      - `tier` (str): Tier description
      - `range_kwh` (str): Range of kWh for this tier
      - `rate_euros_per_kwh` (float): Rate per kWh for this tier
      - `consumption_kwh` (float): Consumption in this tier
      - `cost_euros` (float): Cost for this tier

#### Invalid Input Handling
- Raises **TypeError** if input is not a number
- Raises **ValueError** if input is negative or infinite
- Raises **ValueError** if input is NaN

## Example Usage
```python
result = calculate_electricity_bill(350)
print(result['total_cost_euros'])  # Output: 67.50
```

## Tier Breakdown for 350 kWh
1. First 100 kWh: €0.12/kWh → €12.00
2. Next 100 kWh: €0.18/kWh → €18.00
3. Remaining 150 kWh: €0.25/kWh → €37.50
Total: €67.50

## Implementation Notes
- Use decimal arithmetic internally. Round monetary output to two decimal places using ROUND_HALF_UP, then expose ordinary JSON-compatible numbers. Accept integers and floats as consumption values.
- Always return all three tier entries in order, including tiers with zero consumption. Tier consumption must sum to the supplied consumption.
- The function is pure and has no side effects
- Input validation strictly enforces numeric types and values