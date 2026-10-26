import unittest
from warehouse_box_shipping_calculator_code import calculate_total_cost

class TestCalculateTotalCost(unittest.TestCase):
    
    def test_zero_boxes(self):
        """Test that zero boxes return 0.0"""
        self.assertEqual(calculate_total_cost(0), 0.0)
        
    def test_first_tier(self):
        """Test first tier: 1-10 boxes at EUR 2.00 each"""
        self.assertEqual(calculate_total_cost(1), 7.0)   # 1*2 + 5 = 7
        self.assertEqual(calculate_total_cost(5), 15.0)  # 5*2 + 5 = 15
        self.assertEqual(calculate_total_cost(10), 25.0) # 10*2 + 5 = 25
        
    def test_second_tier(self):
        """Test second tier: 11-20 boxes at EUR 1.50 each"""
        self.assertEqual(calculate_total_cost(11), 26.5) # (10*2 + 1*1.5) + 5 = 26.5
        self.assertEqual(calculate_total_cost(15), 32.5) # (10*2 + 5*1.5) + 5 = 32.5
        self.assertEqual(calculate_total_cost(20), 40.0) # (10*2 + 10*1.5) + 5 = 40
        
    def test_third_tier(self):
        """Test third tier: 21+ boxes at EUR 1.00 each"""
        self.assertEqual(calculate_total_cost(21), 41.0) # (10*2 + 10*1.5 + 1*1) + 5 = 41
        self.assertEqual(calculate_total_cost(27), 47.0) # (10*2 + 10*1.5 + 7*1) + 5 = 47
        self.assertEqual(calculate_total_cost(50), 70.0) # (10*2 + 10*1.5 + 30*1) + 5 = 70
        
    def test_boundary_values(self):
        """Test exact boundary values"""
        self.assertEqual(calculate_total_cost(9), 23.0)
        self.assertEqual(calculate_total_cost(10), 25.0)
        self.assertEqual(calculate_total_cost(19), 38.5)
        self.assertEqual(calculate_total_cost(20), 40.0)
        
    def test_negative_input(self):
        """Test negative input raises ValueError"""
        with self.assertRaises(ValueError):
            calculate_total_cost(-1)
            
    def test_invalid_types(self):
        """Test that invalid types raise TypeError"""
        with self.assertRaises(TypeError):
            calculate_total_cost(1.0)  # integral float
        with self.assertRaises(TypeError):
            calculate_total_cost(1.5)  # fractional count
        with self.assertRaises(TypeError):
            calculate_total_cost("5")  # string
        with self.assertRaises(TypeError):
            calculate_total_cost([5])  # list
        with self.assertRaises(TypeError):
            calculate_total_cost(None)  # None
        with self.assertRaises(TypeError):
            calculate_total_cost(True)   # boolean
        with self.assertRaises(TypeError):
            calculate_total_cost(False)  # boolean
            
    def test_return_type(self):
        """Test that return value is a float"""
        result = calculate_total_cost(5)
        self.assertIsInstance(result, float)
        self.assertIs(type(calculate_total_cost(0)), float)
        self.assertIs(type(calculate_total_cost(27)), float)

if __name__ == '__main__':
    unittest.main()