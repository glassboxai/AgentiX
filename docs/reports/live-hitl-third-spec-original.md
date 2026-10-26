## tiered_energy_bill Specifications

### Function Signature
```python
def tiered_energy_bill(kwh_usage: int) -> int:
    """Calculate a fictional progressive electricity bill in integer cents with tiered pricing.

    Args:
        kwh_usage (int): Nonnegative integer representing kWh consumed.

    Returns:
        int: Total cost in cents.

    Raises:
        ValueError: If input is not a nonnegative integer.
    """
```

### Validation Rules
- Input must be an instance of `int` and >= 0.
- Raises `ValueError` for invalid types or negative values.

### Calculation Logic
- First 100 kWh: 12 cents/unit
- Next 100 kWh: 18 cents/unit
- All kWh beyond 200: 25 cents/unit

### Example
```python
tiered_energy_bill(150)  # 100*12 + 50*18 = 2100 cents
```