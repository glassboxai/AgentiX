# tiered_energy_bill_specifications.md

## Function: tiered_energy_bill

### Description:
Calculates the total electricity bill in integer cents using tiered pricing. The tiers are: first 100 kWh at 12 cents, next 100 kWh at 18 cents, and all remaining kWh at 25 cents.

### Parameters:
- `kwh: float` - The total kilowatt-hours consumed.

### Return Type:
- `int` - The total bill in integer cents.

### Notes:
- Assumes non-negative input values for kWh.
- Calculates the bill by applying the tiered pricing structure and returns the total in integer cents.