def calculate_total_cost(number_of_boxes: int) -> float:
    """
    Calculate the EUR charge to prepare and ship a whole, non-negative number of boxes.
    
    Args:
        number_of_boxes: A non-negative integer representing the number of boxes
        
    Returns:
        The total cost in EUR as a float
        
    Raises:
        TypeError: If input is not an integer (including booleans)
        ValueError: If input is negative
    """
    # Validate input type
    if not isinstance(number_of_boxes, int) or isinstance(number_of_boxes, bool):
        raise TypeError("Input must be an integer")
    
    # Validate non-negative
    if number_of_boxes < 0:
        raise ValueError("Number of boxes cannot be negative")
    
    # No boxes, no charge
    if number_of_boxes == 0:
        return 0.0
    
    # Calculate preparation costs based on progressive tiers
    # First 10 boxes at EUR 2.00 each
    if number_of_boxes <= 10:
        preparation_cost = number_of_boxes * 2.00
    # Next 10 boxes at EUR 1.50 each (boxes 11-20)
    elif number_of_boxes <= 20:
        preparation_cost = (10 * 2.00) + ((number_of_boxes - 10) * 1.50)
    # Additional boxes at EUR 1.00 each (boxes 21+)
    else:
        preparation_cost = (10 * 2.00) + (10 * 1.50) + ((number_of_boxes - 20) * 1.00)
    
    # Add shipping charge
    total_cost = preparation_cost + 5.00
    
    return total_cost