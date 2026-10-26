# Tiered electricity billing specification

Implement exactly one pure standalone public function tiered_energy_bill(kwh: int) -> int. Input kwh must be a nonnegative Python integer; bool is explicitly invalid despite being an int subclass. Reject negative integers, all floats (including 1.0), booleans, strings and None with ValueError. Validate before doing arithmetic.

Return integer cents using progressive bands: first 100 units at 12 cents per unit, next 100 units at 18 cents, all remaining units at 25 cents. No rounding or floating-point arithmetic is needed. No I/O, network, dynamic execution, imports with side effects or third-party packages.

Independent examples: 0 -> 0; 1 -> 12; 99 -> 1188; 100 -> 1200; 101 -> 1218; 199 -> 2982; 200 -> 3000; 201 -> 3025; 250 -> 4250; 1000 -> 23000.

Tests must import the actual generated function, exercise outputs and exact integer return type, cover boundaries and invalid input categories, and use meaningful unittest assertions. Provisional unittest success never replaces human review and independent acceptance cases. Final task: execute for 250 kWh and report 4250 cents (42.50 EUR).
