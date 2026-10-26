# Warehouse Box Shipping Calculator — Reviewed Specifications

## Purpose
Calculate the EUR charge to prepare and ship a whole, non-negative number of boxes using progressive tiers. No external effects, files or network access are needed.

## Public function
`calculate_total_cost(number_of_boxes: int) -> float`

The input must be a Python integer excluding booleans. Reject floats (including integral floats), strings, booleans, None, collections and other non-integer values with TypeError. Reject negative integers with ValueError. Do not silently coerce input.

Return a finite float in EUR. For zero boxes return 0.0, with no shipping charge. For a positive count, charge the first min(count, 10) boxes at EUR 2.00 each; the next min(max(count-10, 0), 10) boxes at EUR 1.50 each; and max(count-20, 0) boxes at EUR 1.00 each. Add EUR 5.00 shipping once. The rates apply only to their portions.

## Independently checked examples
0 -> 0.0; 1 -> 7.0; 9 -> 23.0; 10 -> 25.0; 11 -> 26.5; 19 -> 38.5; 20 -> 40.0; 21 -> 41.0; 27 -> 47.0; 50 -> 70.0.
For 27 boxes: 10*2.00 + 10*1.50 + 7*1.00 + 5.00 = 47.00 EUR.

## Verification requirements
Meaningful unittest assertions must use fixed, independently checked expected values for normal quantities and both sides of each tier boundary, including zero and 27. Verify negative values and invalid types, including True, False and None. Tests must call the implementation rather than duplicate it as an oracle. Submit declarative acceptance cases for human review and host comparison; generated unittest success is provisional. After successful approved validation, execute the function for 27 boxes.

## Human review corrections
The reviewer corrected inconsistent original examples (20 and 27 boxes), a contradictory example comment, the None exception contract and explicit boolean rejection. These edits are reviewer-authored; the original proposal is retained in the live review evidence.
